using System;
using System.Collections.Generic;

namespace room_booking.Models;

public partial class Rezerwacje
{
    public int Id { get; set; }

    public int IdRezerwujacy { get; set; }

    public int IdSala { get; set; }

    public DateTime TerminOd { get; set; }

    public DateTime TerminDo { get; set; }

    public virtual Rezerwujacy IdRezerwujacyNavigation { get; set; } = null!;
}
