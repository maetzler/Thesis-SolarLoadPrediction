# Master Thesis
Code und Notebooks zur Masterarbeit "Erzeugungsprognose für PV-Anlagen - Entwicklung einer kurzfristigen Lastvorhersage mit GIS- und Data Analytics-Methoden" im Rahmen des Universitätslehrganges „Geographical Information Science & Systems“ (UNIGIS MSc) am Fachbereich Geoinformatik (Z_GIS), 
Fakultät für Digitale und Analytische Wissenschaften, Universität Salzburg

**Autor:** Andreas Mätzler  
**Institution:** Universität Salzburg
**Jahr:** 2026  

## Thema
Entwicklung einer kurzfristigen Lastvorhersage mit GIS- und Data Analytics-Methoden

## Gliederung, Notebooks & Skripte
Alle Dateien, Scripts und Verzeichnisse folgen dem **Pipeline-Stage-First (PSF)** Schema:

```
<STAGE><SUBSTAGE>_<BEREICH>_<INHALT>_<DETAIL>.<ext>
```

### Stufendefinition

| Stage | Kürzel | Name | Bereich | Werkzeug |
|---|---|---|---|---|
| 1 | `S1` | Data Export | EVU | Oracle SQL / CMD |
| 2 | `S2` | Spatial Processing | EVU | ArcGIS Pro / Python |
| 3 | `S3` | ETL & Feature Join | EVU | FME Workbench |
| 4 | `S4` | Preprocessing | LOCAL | Python Notebook |
| 5 | `S5` | Modelling & HPO | LOCAL | Python / CatBoost |
| 6 | `S6` | Prediction / CMV | LOCAL | Python / OpenCV |

### Bereich-Kürzel

| Kürzel | Bedeutung |
|---|---|
| `EVU` | Firmennetzwerk – kein öffentlicher Zugriff |
| `LOC` | Lokaler Rechner |

### Konvention: Scripts & Notebooks

```
S<N>[a|b]_<EVU|LOC>_<Inhalt>_<Detail>.<ext>
```

## Datengrundlage

- **PV-Lastprofile:** Viertelstundenwerte 2018, Volleinspeisung, Netzgebiet Vorarlberg
- **Satellitendaten:** Meteosat SEVIRI (EUMETSAT), Bänder VIS006, VIS008, IR039, WV062, IR108 u.a.
- **Globalstrahlung:** Bodenmessung als Referenz-Feature

> Die Rohdaten sind nicht im Repository enthalten (Datenschutz / Dateigröße).

## Technologie-Stack

- Python 3.13.9 · CatBoost · scikit-learn · SHAP
- satpy · pyresample · GDAL · OpenCV
- pandas · numpy · matplotlib · plotly · seaborn

## Lizenz
Dieses Repository enthält ausschließlich Code im Rahmen der akademischen Arbeit.  
Eine kommerzielle Nutzung ist nicht gestattet.
