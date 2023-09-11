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
        }
        static void Main(string[] args)
        {
            List<CityHotel> hotels = new List<CityHotel>
            {
                new CityHotel {City = "Tallinn", Hotel = "Hilton", Address = "Tallinna pst  23", Services= new List<string> {"WiFi", "Parking"}}
            };
        }
    }
}