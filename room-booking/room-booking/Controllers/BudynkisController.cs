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
    public class BudynkisController : ControllerBase
    {
        private readonly RoomBookingContext _context;

        public BudynkisController(RoomBookingContext context)
        {
            _context = context;
        }

        // GET: api/Budynkis
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Budynki>>> GetBudynkis()
        {
          if (_context.Budynkis == null)
          {
              return NotFound();
          }
            return await _context.Budynkis.ToListAsync();
        }

        // GET: api/Budynkis/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Budynki>> GetBudynki(int id)
        {
          if (_context.Budynkis == null)
          {
              return NotFound();
          }
            var budynki = await _context.Budynkis.FindAsync(id);

            if (budynki == null)
            {
                return NotFound();
            }

            return budynki;
        }

        // PUT: api/Budynkis/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutBudynki(int id, Budynki budynki)
        {
            if (id != budynki.Id)
            {
                return BadRequest();
            }

            _context.Entry(budynki).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!BudynkiExists(id))
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

        // POST: api/Budynkis
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Budynki>> PostBudynki(Budynki budynki)
        {
          if (_context.Budynkis == null)
          {
              return Problem("Entity set 'RoomBookingContext.Budynkis'  is null.");
          }
            _context.Budynkis.Add(budynki);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetBudynki", new { id = budynki.Id }, budynki);
        }

        // DELETE: api/Budynkis/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteBudynki(int id)
        {
            if (_context.Budynkis == null)
            {
                return NotFound();
            }
            var budynki = await _context.Budynkis.FindAsync(id);
            if (budynki == null)
            {
                return NotFound();
            }

            _context.Budynkis.Remove(budynki);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool BudynkiExists(int id)
        {
            return (_context.Budynkis?.Any(e => e.Id == id)).GetValueOrDefault();
        }
    }
}
