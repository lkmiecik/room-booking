using System;
using System.Collections.Generic;

namespace room_booking.Models;

public partial class Sale
{
    public int Id { get; set; }

    public string Name { get; set; } = null!;

    public int Pojemnosc { get; set; }

    public string Wyposazenie { get; set; } = null!;

    public byte Niepelnospr { get; set; }

    public int Pietro { get; set; }

    public int IdBudynek { get; set; }

    public virtual Budynki IdBudynekNavigation { get; set; } = null!;
}
