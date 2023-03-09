using System;
using System.Collections.Generic;

namespace room_booking.Models;

public partial class Rezerwujacy
{
    public int Id { get; set; }

    public string FirstName { get; set; } = null!;

    public string LastName { get; set; } = null!;

    public virtual ICollection<Rezerwacje> Rezerwacjes { get; } = new List<Rezerwacje>();
}
