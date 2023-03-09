using System;
using System.Collections.Generic;

namespace room_booking.Models;

public partial class Budynki
{
    public int Id { get; set; }

    public string Name { get; set; } = null!;

    public virtual ICollection<Sale> Sales { get; } = new List<Sale>();
}
