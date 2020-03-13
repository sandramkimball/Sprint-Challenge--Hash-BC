# One-Way Flight Trip

You've booked a _really_ cheap one-way flight. Unfortunately, that means you have _tons_ of layovers before you reach your destination. The morning of, you woke up late and had to scramble to the airport to catch your first flight. However, in your rush, you accidentally scrambled all your flight tickets. You don't know the route of your entire trip now!

Write a function `reconstruct_trip` to reconstruct your trip from your mass of flight tickets. Each ticket is represented as a Class with the following form:
```
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
```
where the `source` string represents the starting airport and the `destination` string represents the next airport along our trip. The ticket for your first flight has a destination with a `source` of `NONE`, and the ticket for your final flight has a `source` with a `destination` of `NONE`. 

Pseudocode for an array of `Tickets` might look like this:

```
tickets = [
  Ticket{ source: "PIT", destination: "ORD" },
  Ticket{ source: "XNA", destination: "CID" },
  Ticket{ source: "SFO", destination: "BHM" },
  Ticket{ source: "FLG", destination: "XNA" },
  Ticket{ source: "NONE", destination: "LAX" },
  Ticket{ source: "LAX", destination: "SFO" },
  Ticket{ source: "CID", destination: "SLC" },
  Ticket{ source: "ORD", destination: "NONE" },
  Ticket{ source: "SLC", destination: "PIT" },
  Ticket{ source: "BHM", destination: "FLG" }
]
```



Your solution should run in linear time. 

## Hints
* 'Link' tickets together to reconstruct the trip. 

* Hash each ticket so that the starting location is the key and the destination is the value. 

* Construct entire route, the `i`th location in the route can be found by checking the hash table for the `i-1`th location.

* Cleanup at the end to make sure results match what's expected.