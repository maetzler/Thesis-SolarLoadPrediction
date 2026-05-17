# Solar Load Prediction – Master Thesis
Code und Notebooks zur Masterarbeit "Erzeugungsprognose für PV-Anlagen" im Rahmen des Universitätslehrganges „Geographical Information Science & Systems“ (UNIGIS MSc) am Fachbereich Geoinformatik (Z_GIS), 
Fakultät für Digitale und Analytische Wissenschaften, Universität Salzburg

**Autor:** Andreas Mätzler  
**Institution:** Universität Salzburg
**Jahr:** 2026  

## Thema
Entwicklung einer kurzfristigen Lastvorhersage mit GIS- und Data Analytics-Methoden

## Gliederung, Notebooks & Skripte

| #  | Beschreibung
| 01 | Oracle SQL – Export der PV-Lastprofile (2018) aus dem Energiedatenmanagementsystem
| 02 | Konvertierung der EUMETSAT SEVIRI NAT-Dateien in GeoTIFF (multithreaded, Clip auf Vorarlberg / Bodenseeregion)
| 03 | Feature-Extraktion: SEVIRI-Bandwerte je PV-Anlage und Zeitstempel
| 04 | Datenvorverarbeitung und Feature Engineering
| 05 | Kurzfristprognose der SEVIRI-Wolkenbewegung mittels OpenCV Optical Flow
| 06 | CatBoost-Regression mit Rolling-Window Cross-Validation und Random Search Hyperparameter-Optimierung

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
