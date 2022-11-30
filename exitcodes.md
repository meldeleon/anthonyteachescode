## exitcodes
- if something is succesful in commands it generally returns 0, any other number is usually a problem.
- sometimes commands uses helpful status exit codes (puppet does this).
- special exit codes (common)
  - 127 (bash), command not found.
  - 137, process was killed. 128 + n, n is a signal number.
- man pages often will document exitcodes.    
