SET ECHO OFF
SET VERIFY OFF
SET TRIMSPOOL ON
SET TRIMOUT ON
SET LINESIZE 9999
SET PAGESIZE 0
SET FEEDBACK OFF
SET TIMING OFF
SET TIME OFF
SET LONG 10000
set arraysize 5000
SET TERMOUT OFF
alter session  set NLS_NUMERIC_CHARACTERS= '.,';
spool .\Solar_Load_Profile_alle_Volleinspeiser_2018.csv

select 'NEI_ID;HAUS_ID;ZP_ID;TIMESTAMP;WERT' from dual;

select NEI_ID||';'||NEI_HAUS_ID||';'||LP_ZP_ID||';'||to_char(LP_TIMESTAMP-INTERVAL '1' HOUR,'YYYY-MM-DD HH24:MI:SS')||';'||TO_CHAR(LP_WERT)
  from EDM_LP_DATEN t,
       EDM_ZAEHLPUNKT ZP,
       (select nei_zaehlerpunktbezeichnung, NEI_HAUS_ID, NEI_ID
          from bmi_netzeinspeiser@db14 NEI
         where nei_isu_energietraeger = 'Photovoltaik'
           and nei_einsatzart = 'Volleinspeisung'
           and NEI_FERNAUSLESBARKEIT = 'J')
 where lp_zp_id = zp_id
   and LP_WERT > 0
   and substr(zp_zaehlpunkt, 0, 33) = nei_zaehlerpunktbezeichnung
   and (substr(zp_zaehlpunkt, 34, 3) = ' P-' OR length(zp_zaehlpunkt) = 33)
   and LP_TIMESTAMP between '01.01.2018' and '01.01.2019';
prompt sysdate
spool off
set head on
set feed 6
quit
