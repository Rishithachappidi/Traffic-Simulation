# Manual smoke-test checklist

This is a checklist, not a record of completed tests.
Record the operating system, Python version, and Pygame version.

- [ ] Start the simulation from the repository root.
- [ ] Confirm the window opens and assets load.
- [ ] Observe vehicles spawning and moving.
- [ ] Observe traffic-signal transitions.
- [ ] Observe crossed-vehicle counters updating.
- [ ] Check the console for exceptions.
- [ ] Close the window and check whether the process exits.

For failures, record reproduction steps and the traceback.

## Timed run

Run `python run_simulation.py --duration 5 --seed 42`. Confirm the window closes on its own, the terminal reports crossing counts and throughput, and the process exits with status 0. Repeat and press Escape to check early exit.
