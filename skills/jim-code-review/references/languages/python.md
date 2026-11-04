# Python

Load for Python changes. Read the supported Python version, package metadata, environment assumptions, and test configuration before making compatibility claims.

- Trace exception handling and return values through the whole operation. Look for swallowed failures, partial writes, and misleading success; a broad exception handler is not itself a defect when recovery is deliberate and complete.
- Check shared mutable defaults, aliasing, iterators consumed more than once, and mutation during iteration against an actual call sequence. Distinguish intended caching from accidental shared state.
- Inspect files, temporary directories, generators, database connections, and tasks across early exits. Establish an actual lifetime/resource problem before requiring a context manager.
- Trace externally controlled input into subprocess execution, paths, deserialization, SQL, or template evaluation. Check argument boundaries and existing validation; do not assume every subprocess call invokes a shell.
- For asynchronous or threaded code, inspect blocking operations, cancellation, task failures, and shared state under the chosen execution model. Do not assume the interpreter makes compound state updates safe.
- Check path handling, encoding, import/package layout, and dependency/API availability on declared targets. Avoid imposing a formatter, type checker, virtual environment manager, or packaging tool the project does not use.
