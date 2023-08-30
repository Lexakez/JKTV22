using System;

namespace HelloApp
{
    class Program
    {
        class Student
        {
            //Переменные
            public string firstname;
            public string lastname;
            public string group;
            public Student()
            {

            }
            //Variant2
            public Student(string firstname, string lName)
            {
                this.firstname = firstname;
                lastname = lName;
                group = "JPTVR19";
            }
            //Variant3
            public Student(string firstname, string lName, string group)
            {
                this.firstname = firstname;
                this.lastname = lName;
                this.group = group;
            }
            public void GetInfo()
            {
                Console.WriteLine($"\n\nStudent: {firstname} - {lastname}, Group: {group}");
            }
        }
        //end class
        static void Main(string[] args)
        {   //variant1
            Console.WriteLine("\nVariant1");
            var str = new string('=', 20);
            Student stud = new Student();
            stud.firstname = "Anna";
            stud.lastname = "Petrova";
            stud.group = "JPTVR18";
            stud.GetInfo();
            //variant2
            Console.WriteLine("\nVariant2");
            Console.WriteLine(str);
            Student stud1 = new Student("Jelena", "Sokolova");
            stud1.GetInfo();
            //variant3
            Console.WriteLine("\nVariant3");
            Console.WriteLine(str);
            Student stud2 = new Student("Maria", "Tukova", "JPTV20");
            stud2.GetInfo();
            Console.Write("\n\nPress any key...");
            Console.ReadKey();
        }
    }
}
