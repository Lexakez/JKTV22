using System;
using System.Linq;
using System.Collections.Generic;

namespace StudentListApp
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] names = { "Ivanov", "Ivanova", "Petrov", "Pavlov", "Djatlov", "Sidorov", "Abramov", "Kirov", "Svetlov", "Aronova", "Akulov" };
            Console.WriteLine("\n\n Student list");
            int k = 0;
            foreach (string nameOne in names)
            {
                k++;
                Console.WriteLine(k + ". " + nameOne);
            }
            k = 0;
            Console.WriteLine(string.Concat(Enumerable.Repeat("=", 20)));
            Console.WriteLine("\n\nVariant 1. Array");
            var selectedNames = new List<string>();
            foreach (string s in names)
            {
                if (s.ToUpper().StartsWith("A")) selectedNames.Add(s);
            }
            selectedNames.Sort();
            foreach (string s in selectedNames)
            {
                k++;
                Console.WriteLine(k + ". " + s);
            }
            k = 0;
            Console.WriteLine(string.Concat(Enumerable.Repeat("=", 20)));
            Console.WriteLine("\n\nVariant 2. LINQ");
            var namesA = from n in names
                         where n.StartsWith("A")
                         orderby n
                         select n;
            foreach (string item in namesA)
            {
                k++;
                Console.WriteLine(k + ". " + item);
            }
            k= 0;
            Console.WriteLine(string.Concat(Enumerable.Repeat("=", 20)));
            Console.WriteLine("\n\nVariant 3.");
            var selectedNamesTwo = names.Where(n => n.StartsWith("A")).OrderBy(n => n);
            foreach (string item in selectedNamesTwo)
            {
                k++;
                Console.WriteLine(k +". " +item);
            }
            Console.Write("\n\nPress any key...");
            Console.ReadKey();
        }     
    }
}
