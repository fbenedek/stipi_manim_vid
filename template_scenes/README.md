# Mintajelenetek

A videósorozatban használt intro és outro jelenetek közös változatai. Módosítva a saját beállításaitokat a  beállításokat tartamazó `.json` fájlokban, `IntroOutroScenes.py` futtatásával könnyen elkészíthetitek nyitányotokat vagy záró képsorotokat, állítható címmel, dátummal stb. Egy minta generáláshoz futtasd a kövvetkezőt:
    <bash>
        manimgl IntroOutroScenes.py IntroScene
    </bash>
A kimenetet megtalálod a `../stipi_manim_vid/media/out/IntroScene.mp4` videófájlban. Elvileg így néz ki:
- TODO: kép beillesztése ide!
Ha a minta megegyezik azzal a példával, amit a képen látsz, nekiláthatsz saját intro/outro-d elkészítésének. Az intro beállításaihoz módosítsd az `intro_settings.json` megfelelő mezőit:
- A videó címét a `title` mezőben,
- a videó alcímét a `headline` mezőben,
- a kimenet fájlnevét a `out_file` mezőben (a kiterjesztés ne maradjon le!),
- a készítés dátumát a `date` mezőben, `ÉÉÉÉ. HÓNAP NN.` formátumban adhatod meg.
- A `media` mező pozícionálja a címet annak függvényében, hogy hozzáadsz-e saját nyitó animációt, vagy nem. Ha csak gyorsan szeretnél egyedi megjelenést adni a videódnak, add meg a `png` értéket ennek a mezőnek, és a program a `media_path` elérési úton található `.png` fájlt betöltve megjeleníti a képet a cím alatt. Ha a `custom` értéket adod a `media` mezőnek, a program magasabbra tolja a címet, de mást nem csinál; ahhoz, hogy megjelenjen valami, módosítsd a IntroScene osztály custom_animation tagfüggvényét. Ha a `media` mező a `blank` értéket kapja, a címet középre tolja, és nem jelenít meg semmi mást a footeren kívül.

Az outro-t is hasonlóan változtathatod az `outro_setting.json` fájl módosításával:
- A `cast` listában megadhatod a készítők neveit és a munkában betöltött szerepüket (további infóért lásd a mintát a fájlban),
- A `thanks_to` mezőben megváltoztathatod a stáblista köszönetnyilvánítását a Stipinek.

