using System;
using System.Linq;
using System.Collections.Generic;

namespace CityHotelsApp
{
    class Program
    {
        class CityHotel
        {
            public string City { get; set; }
            public string Hotel { get; set; }
            public string Address { get; set; }
            public List<string> Services { get; set; }
            public CityHotel()
            {
                Services = new List<string>();
            }
        }
        static void Main(string[] args)
        {
            List<CityHotel> hotels = new List<CityHotel>
            {
                new CityHotel {City = "Tallinn", Hotel = "Hilton", Address = "Tallinna pst  23", Services= new List<string> {"WiFi", "Parking"}},
                new CityHotel {City = "Tallinn", Hotel = "Merres", Address ="Tallina mnt 01", Services= new List<string> {"WiFi", "Parking"}},
                new CityHotel {City = "Tallinn", Hotel = "Junina", Address = "Tallinna pst 22", Services = new List<string> {"WiFi", "Bar", "Parking"}},
                new CityHotel {City = "Tartu", Hotel = "Messia", Address = "Tartu center 22", Services = new List<string> {"WiFi", "Bar", "Parking"}},
                new CityHotel {City = "Tartu", Hotel = "Tartu center hostel", Address = "Tartu mnt 41", Services =new List<string> {"WiFi", "Bar"}},
                new CityHotel {City = "Parnu", Hotel = "Parnu hostel", Address = "Parnu mnt 14", Services = new List<string>{"Parking", "WiFi"}},
                new CityHotel {City = "Parnu", Hotel = "Parnu Hiusa hostel", Address = "Parnu heina 28", Services = new List<string>{"WiFi","Parking"}},
                new CityHotel {City = "Toila", Hotel = "Toila spa hotel", Address = "Toila raida 13", Services = new List<string>{"WiFi", "Parking", "Spa" }}
            };
            var selectedHotel = from h in hotels
                                select h;
            Console.WriteLine("Hotel List\n");
            //Console.WriteLine("City: \t \tName:\t\tAddress:\t\t\tSrvices:");

            foreach (CityHotel h in selectedHotel)
            {
                Console.Write($"City: {h.City} - Hotel Name: {h.Hotel} - Address: {h.Address} - Services: ");
                    foreach (var serv in h.Services)
                    {
                        Console.Write($"{serv} ");
                    }
                Console.WriteLine("");

            }
        }
    }
}