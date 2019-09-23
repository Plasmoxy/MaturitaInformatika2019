/** sebu petrik
 * prikald vystupu
 * 
 *  [50%] Building C object CMakeFiles/slova.dir/slova.c.o
    [100%] Linking C executable slova
    [100%] Built target slova
    Kededi jinedu ki hawi volebi.Fi dedu lasusi bepomi womewe he nu.
    Dukeve niwozu topepe pu caki hicuhu ca site.Le duju wine zavefu jefomo na wido.
    Buso vefoki lapore gevuko vegu ma ronu.Gabuxu biga kareli zara.Juga rivo vusimu xohosi voga bi kega.
    Li sisi xasoco pufa joze pa zu vime juto.Vawu vovufu wekota.Hewa no hata.

**/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>

const char SPOLUHLASKY[] = "bcdfghjklmnprstvwxz";
const char SAMOHLASKY[] = "aeiou";
const size_t SAM_SIZE = sizeof(SAMOHLASKY);
const size_t SPO_SIZE = sizeof(SPOLUHLASKY);

char randSpoluhlaska() {
    return SPOLUHLASKY[rand() % (SPO_SIZE-1)];
}

char randSamohlaska() {
    return SAMOHLASKY[rand() % (SAM_SIZE-1)];
}

char * randSlovo(int pocetHlasok) {
    static char * slovo;
    slovo = malloc(pocetHlasok * sizeof(char));

    for (int i = 0; i < pocetHlasok*2; i += 2) {
        slovo[i] = randSpoluhlaska();
        slovo[i+1] = randSamohlaska();
    }

    return slovo;
}

char * randVeta(int pocetSlov) {
    static char * veta;
    int velkostSlov[pocetSlov];
    int velkostVety = 0;
    
    // vypocet velkosti vety a slov
    for (int i = 0; i < pocetSlov; i++) {
        velkostSlov[i] = ((rand() % 3)+1)*2; // iba parne velkosti
        velkostVety += velkostSlov[i]; // pridaj velkost slova
        velkostVety += 1; // 1 znak za medzeru
    }

    // alokovanie pamati pre vetu
    veta = malloc(velkostVety*sizeof(char));

    // vytvorenie a prekopirovanie slov do vety
    for (int i = 0; i < pocetSlov; i++) {
        char * slovo = randSlovo(velkostSlov[i]/2);
        if (i == 0) {
            slovo[0] = toupper(slovo[0]);
        }

        strcat(veta, slovo);

        if (i == pocetSlov-1) {
            strcat(veta, ".");
        } else {
            strcat(veta, " ");
        }
    }

    return veta;
}

char * randSlohovyUtvar(int pocetViet) {
    static char *sloh;
    size_t slohSize = 0;
    char *vety[pocetViet]; // array pointerov na char, medzery su akoby samostatne vety s pointerom
    
    // vytvaranie viet
    for (int i = 0; i < pocetViet; i++) {
        vety[i] = randVeta((rand() % 7) + 3); // medzi 3 a 10 slovami
        slohSize += strlen(vety[i]); // velkost viet
    }

    slohSize += 1; // terminator na koniec
    sloh = malloc(slohSize * sizeof(char));

    for (int i = 0; i < pocetViet; i++) {
        strcat(sloh, vety[i]);
    }

    return sloh;
    
}

int main() {
    srand(time(NULL));
    char *utvar = randSlohovyUtvar(10);
    printf("%s\n", utvar);
}