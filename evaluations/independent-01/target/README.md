# Utility modules

These independent modules are proposed additions for a small local application. Each exports an operation called `apply`; files do not call each other. There is no web server or multi-user permission boundary.

Python 3.12+ is supported. SQLite callers pass an idle default-configuration sqlite3 connection with committed initial rows; no enclosing transaction is active. Database exceptions propagate to the caller. The `notes` table has `id INTEGER PRIMARY KEY, title TEXT`, and IDs 1 and 2 exist. A write can fail independently of earlier writes.

JavaScript runs in Node 22+. Save acknowledgment inputs are plain records with exactly `id`, `content`, and `modified_at`. `submitted` is the snapshot sent to persistence; `saved` is that same snapshot with the database's timestamp. `current` is the record presently in the editor, possibly with later typing. The function returns replacement editor state; preserve later edits and acknowledge the timestamp if submitted content is still current. IDs identify records.

Pagination inputs are arrays and a limit. Limits are nonnegative integers, null, or undefined; null/undefined mean 10. Zero explicitly requests no results. The caller treats the returned list as the result page. No negative or noninteger limits are accepted by callers.

Review the new modules against their contracts and the relevant function docstrings. No external dependencies or services are needed to reason about them.
