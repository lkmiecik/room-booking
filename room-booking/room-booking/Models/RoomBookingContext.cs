using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace room_booking.Models;

public partial class RoomBookingContext : DbContext
{
    public RoomBookingContext()
    {
    }

    public RoomBookingContext(DbContextOptions<RoomBookingContext> options)
        : base(options)
    {
    }

    public virtual DbSet<Budynki> Budynkis { get; set; }

    public virtual DbSet<Rezerwacje> Rezerwacjes { get; set; }

    public virtual DbSet<Rezerwujacy> Rezerwujacies { get; set; }

    public virtual DbSet<Sale> Sales { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. You can avoid scaffolding the connection string by using the Name= syntax to read it from configuration - see https://go.microsoft.com/fwlink/?linkid=2131148. For more guidance on storing connection strings, see http://go.microsoft.com/fwlink/?LinkId=723263.
        => optionsBuilder.UseSqlServer("Server=(localdb)\\MSSQLLocalDB;Database=room_booking;Trusted_Connection=True;");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Budynki>(entity =>
        {
            entity.ToTable("budynki");

            entity.Property(e => e.Id).HasColumnName("ID");
            entity.Property(e => e.Name)
                .HasColumnType("text")
                .HasColumnName("name");
        });

        modelBuilder.Entity<Rezerwacje>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("PK__rezerwac__3214EC2733F9C9BD");

            entity.ToTable("rezerwacje");

            entity.Property(e => e.Id)
                .ValueGeneratedNever()
                .HasColumnName("ID");
            entity.Property(e => e.IdRezerwujacy).HasColumnName("id_rezerwujacy");
            entity.Property(e => e.IdSala).HasColumnName("id_sala");
            entity.Property(e => e.TerminDo)
                .HasColumnType("date")
                .HasColumnName("termin_do");
            entity.Property(e => e.TerminOd)
                .HasColumnType("date")
                .HasColumnName("termin_od");

            entity.HasOne(d => d.IdRezerwujacyNavigation).WithMany(p => p.Rezerwacjes)
                .HasForeignKey(d => d.IdRezerwujacy)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("FK_rezerwacje_ToTable");
        });

        modelBuilder.Entity<Rezerwujacy>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("PK__rezerwuj__3214EC27130996F4");

            entity.ToTable("rezerwujacy");

            entity.Property(e => e.Id).HasColumnName("ID");
            entity.Property(e => e.FirstName)
                .HasColumnType("text")
                .HasColumnName("first_name");
            entity.Property(e => e.LastName)
                .HasColumnType("text")
                .HasColumnName("last_name");
        });

        modelBuilder.Entity<Sale>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("PK__sale__3214EC27DDB2FA40");

            entity.ToTable("sale");

            entity.Property(e => e.Id).HasColumnName("ID");
            entity.Property(e => e.IdBudynek).HasColumnName("id_budynek");
            entity.Property(e => e.Name)
                .HasColumnType("text")
                .HasColumnName("name");
            entity.Property(e => e.Niepelnospr).HasColumnName("niepelnospr");
            entity.Property(e => e.Pietro).HasColumnName("pietro");
            entity.Property(e => e.Pojemnosc).HasColumnName("pojemnosc");
            entity.Property(e => e.Wyposazenie)
                .HasColumnType("text")
                .HasColumnName("wyposazenie");

            entity.HasOne(d => d.IdBudynekNavigation).WithMany(p => p.Sales)
                .HasForeignKey(d => d.IdBudynek)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("FK_sale_ToTable");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
