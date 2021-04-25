# svg-diff

Algorithmus zur Detektion von Ähnlichkeiten in SVG Pfaden

Die Funktion `diffSvgs` nimmt zwei iterables mit SVG Pfaden entgegen und liefert einen Wahrheitswert der angibt ob sich die SVGs ähnlich sind.

Die Vergleiche sind aktuell nur für Pfade die Kurven enthalten aussagekräftig, weitere Checks müssen noch implementiert werden hinzugefügt werden.

Grundidee: Das zu findende SVG (erster Parameter) wird in 45° Schritten gedreht. Jeder Schritt wird jeweils getestet. Für die enthaltenen Pfade werden Tangenten berechnet (Auflösung aktuell 100 Schritte pro Pfad). Der Algorithmus soll vergleichen, ob Pfadverläuft ähnlich sind, daher vergleichen wir die Unterschiede zwischen den jeweiligen Tangenten (daher funktioniert die aktuelle Version auch nur mit Kurven!).
Die Differenzen der Tangentialvektoren können nun zwischen zwei Pfaden verglichen werden. Sind zwei Pfade ähnlich haben sie an ähnlichen Stellen Kurven in ähnliche Richtungen.

Durch dieses Vorgehen sind wir je nach Kurvenart und gewählter Auflösung und Grenzwerten in der Lage auch skalierte Elemente als gleich zu identifizieren.

## Ideen für Geraden (Lines):

Bei geraden sollte der Winkel als Vergleichswert verwendet werden. Da ein Piktogramm immer aus mehreren Formen besteht wäre die Summer der geraden die gleiche Richtungen zeigen wie Geraden im Referenzbild ein Messwert für Ähnlichkeit.

## Probleme:

In den SVGs sind die Pfade nicht immer identisch. Die Grenzwerte müssen also sinnvoll gewählt werden um keine false negatives zu haben. Desto mehr Formen sinnvoll unterstützt werden, desto unwahrscheinlicher werden vermutlich false positives. In der aktuellen Version stimmen Linien immer überein, sodass der Grenzwert gerade bei Formen mit vielen Geraden recht knapp gewählt werden muss.
