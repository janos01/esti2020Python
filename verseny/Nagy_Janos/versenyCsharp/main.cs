using System;
using System.IO;
using System.Collections.Generic;

class Program01 {
    static List<Verseny> readFile() {
        List<Verseny> versenyek = new List<Verseny>();
		StreamReader  sr = File.OpenText("versenyek.txt");
		string line = null; 
        sr.ReadLine();
		while ((line = sr.ReadLine()) != null) {        
            string[] lineArray = line.Split(':');
            versenyek.Add(new Verseny(
                Convert.ToInt32(lineArray[0]),
                lineArray[1],
                lineArray[2],
                lineArray[3],
                Convert.ToInt32(lineArray[4])
            ));
        }
		sr.Close();
        return versenyek;
   }
   static void feladat2(List<Verseny> versenyek){
       int darab = 0;
       foreach(Verseny verseny in versenyek) {
           if (verseny.az == 5) {
               darab += 1;
           }
       }
       Console.WriteLine("Az 5-ös versenyző ennyi versenyen volt: " + darab);
   }
   static void Main() {
       List<Verseny> versenyek = readFile();
       feladat2(versenyek);
   }
}
