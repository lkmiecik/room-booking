using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using room_booking.Models;

namespace room_booking.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class RezerwujaciesController : ControllerBase
    {
        private readonly RoomBookingContext _context;

        public RezerwujaciesController(RoomBookingContext context)
        {
            _context = context;
        }

        // GET: api/Rezerwujacies
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Rezerwujacy>>> GetRezerwujacies()
        {
          if (_context.Rezerwujacies == null)
          {
              return NotFound();
          }
            return await _context.Rezerwujacies.ToListAsync();
        }

        // GET: api/Rezerwujacies/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Rezerwujacy>> GetRezerwujacy(int id)
        {
          if (_context.Rezerwujacies == null)
          {
              return NotFound();
          }
            var rezerwujacy = await _context.Rezerwujacies.FindAsync(id);

            if (rezerwujacy == null)
            {
                return NotFound();
            }

            return rezerwujacy;
        }

        // PUT: api/Rezerwujacies/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutRezerwujacy(int id, Rezerwujacy rezerwujacy)
        {
            if (id != rezerwujacy.Id)
            {
                return BadRequest();
            }

            _context.Entry(rezerwujacy).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!RezerwujacyExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Rezerwujacies
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Rezerwujacy>> PostRezerwujacy(Rezerwujacy rezerwujacy)
        {
          if (_context.Rezerwujacies == null)
          {
              return Problem("Entity set 'RoomBookingContext.Rezerwujacies'  is null.");
          }
            _context.Rezerwujacies.Add(rezerwujacy);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetRezerwujacy", new { id = rezerwujacy.Id }, rezerwujacy);
        }

        // DELETE: api/Rezerwujacies/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteRezerwujacy(int id)
        {
            if (_context.Rezerwujacies == null)
            {
                return NotFound();
            }
            var rezerwujacy = await _context.Rezerwujacies.FindAsync(id);
            if (rezerwujacy == null)
            {
                return NotFound();
            }

            _context.Rezerwujacies.Remove(rezerwujacy);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool RezerwujacyExists(int id)
        {
            return (_context.Rezerwujacies?.Any(e => e.Id == id)).GetValueOrDefault();
        }
    }
}
