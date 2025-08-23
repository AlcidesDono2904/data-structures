Instructions
Implement the program in Python for each of the following statements.

Exercise #1 - Delete in a doubly linked list
Based on the doubly linked list example shown in class, add a method named `delete` that receives the value to remove from the list. If the value exists, remove the node from the list. Otherwise, print an error message.

## Exercise #2 - Event agenda compression
During a festival, many short events are registered in different rooms. You must merge consecutive events in the same room when the second one starts exactly when the first one ends. Preserve the relative order of the remaining events.

The program will receive the name of a .json file on the command line. The file contains an array of objects with:

- "inicio": string in "HH:MM" format
- "duracion": integer in minutes
- "sala": string (room ID)

Example events.json:

[
  { "inicio": "09:00", "duracion": 60, "sala": "A" },
  { "inicio": "10:00", "duracion": 30, "sala": "A" },
  { "inicio": "10:30", "duracion": 45, "sala": "B" },
  { "inicio": "10:30", "duracion": 30, "sala": "A" },
  { "inicio": "11:00", "duracion": 30, "sala": "A" }
]

Output

A JSON array with the resulting events, preserving relative order.

Expected output for the example:

[
  { "inicio": "09:00", "duracion": 90, "sala": "A" },
  { "inicio": "10:30", "duracion": 45, "sala": "B" },
  { "inicio": "10:30", "duracion": 60, "sala": "A" }
]

Notes

- Only merge adjacent events in the same room when next_start == previous_end.
- Do not reorder the list.
- Use any linear data structure(s) you prefer to solve the problem.
- The JSON filename is provided as a command-line argument.

## Exercise #3 - Cafeteria queue with special rules
In a futuristic cafeteria, a sequence of people arrive with a tag:

- VIP: inserted just before the first non-VIP in the queue (so before NORM and BULK).
- BULK: always placed at the absolute end of the queue; BULK arrivals form a trailing block.
- NORM: placed at the end of the non-BULK zone, i.e., just before the first BULK if any exist.

Write a program that processes all arrivals and returns the final service order.

Notes

- Use any linear data structure(s) you prefer to solve the problem.
- The JSON filename is provided as a command-line argument.

Example comedor.json:

[
  { "tipo": "NORM", "nombre": "Alice" },
  { "tipo": "VIP",  "nombre": "Bob" },
  { "tipo": "NORM", "nombre": "Charlie" },
  { "tipo": "BULK", "nombre": "Dave" },
  { "tipo": "VIP",  "nombre": "Eve" }
]

Program output

For the example JSON above the program output would be: Bob Eve Alice Charlie Dave

(Because each VIP is inserted before the first non-VIP; BULK always stays at the end.)

## Exercise #4 - Delivery drone with exact return
A delivery drone executes instructions read from a file. When it encounters `RETURN`, it must exactly retrace its path in reverse order to return to the starting point. Your task is to print the sequence of actions for the return (the inverse of moves and turns performed before `RETURN`).

Instruction model for the drone:

{"cmd": "MOVE", "x": <integer_meters>}
{"cmd": "TURN_LEFT"}
{"cmd": "TURN_RIGHT"}
{"cmd": "DROP"} (does not affect position; ignored during return)
{"cmd": "RETURN"} (when read, generate/emit inverse actions until back at start)

Notes

- Use any linear data structure(s) you prefer to solve the problem.
- The JSON filename is provided as a command-line argument.

Inverse rules

- Inverse of MOVE x → "MOVE_BACK"
- Inverse of TURN_LEFT → TURN_RIGHT
- Inverse of TURN_RIGHT → TURN_LEFT
- DROP does not generate an inverse action.
- RETURN is not printed; it only triggers the return sequence.

Example dron.json:

[
  { "cmd": "MOVE", "x": 100 },
  { "cmd": "TURN_RIGHT" },
  { "cmd": "MOVE", "x": 50 },
  { "cmd": "DROP" },
  { "cmd": "MOVE", "x": 30 },
  { "cmd": "TURN_LEFT" },
  { "cmd": "MOVE", "x": 20 },
  { "cmd": "DROP" },
  { "cmd": "RETURN" }
]

Program output

Based on the example above, the program output would be:

MOVE_BACK x 20
TURN_RIGHT
MOVE_BACK x 30
MOVE_BACK x 50
TURN_LEFT
MOVE_BACK x 100