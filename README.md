# Conway's Game of Life - GitHub Actions Edition

A self-evolving implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) that runs entirely on GitHub Actions!

## What is this?

This repository uses GitHub Actions to simulate Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The game evolves based on simple rules, creating fascinating patterns from initial configurations.

## How it works

1. **Game State**: The current state of the game is stored in `game_state.txt`
   - `█` represents alive cells
   - `·` represents dead cells

2. **Evolution Script**: `conway.py` implements the Game of Life rules:
   - Any live cell with 2-3 live neighbors survives
   - Any dead cell with exactly 3 live neighbors becomes alive
   - All other cells die or stay dead

3. **GitHub Actions**: The workflow `.github/workflows/conway-game-of-life.yml`:
   - Runs on a **cron schedule** (every hour)
   - Executes the evolution script entirely in the cloud
   - Commits the new generation automatically
   - Creates a living, breathing simulation that evolves on its own!

## Triggering the simulation

The game evolves **entirely through GitHub Actions**:

1. **Automatic evolution**: Runs every hour via cron schedule
2. **Manual trigger**: Go to Actions → Conway's Game of Life → Run workflow
   - You can specify the number of generations to evolve at once
   - Default is 1 generation per run

No local execution needed - it's all in the cloud! ☁️

## Initial patterns

The initial state includes several classic patterns:

- **Glider**: A small pattern that moves diagonally across the grid
- **Blinker**: Oscillates between two states
- **Toad**: Another oscillator with a period of 2
- **Beacon**: A period-2 oscillator
- **Lightweight Spaceship (LWSS)**: Travels across the grid

## Grid topology

The grid uses toroidal (wraparound) topology, meaning:
- Cells on the right edge are neighbors with cells on the left edge
- Cells on the top edge are neighbors with cells on the bottom edge

This creates an infinite looping plane without boundaries.

## Viewing the evolution

To watch the game evolve:

1. Check the [Actions tab](../../actions) to see each generation run
2. View the commit history to see how patterns change over time
3. Look at `game_state.txt` to see the current state

## Watch it live!

The best part? You can watch the game evolve in real-time through GitHub:

1. **Commit History**: Each evolution creates a new commit - watch the timeline grow!
2. **Actions Tab**: See each generation being calculated in the workflow runs
3. **Diff View**: Compare commits to see exactly which cells changed

## Technical details

- **Grid size**: 30 rows × 60 columns
- **Language**: Python 3.11
- **Workflow**: GitHub Actions with cron scheduling
- **Evolution frequency**: Every hour (configurable in the workflow)
- **Grid topology**: Toroidal (wraparound edges)
- **Execution**: 100% in GitHub Actions - no local runs required!

## Customization

Want to experiment? You can:

- Modify the initial patterns in `conway.py`
- Change the grid size
- Adjust the cron schedule (faster or slower evolution)
- Add more interesting patterns (pulsar, gosper glider gun, etc.)
- Change the cell characters to anything you like!

## License

This is a demonstration project showing creative use of GitHub Actions. Feel free to fork and experiment!

## Credits

Inspired by the endless creativity of Conway's Game of Life and the automation possibilities of GitHub Actions.
