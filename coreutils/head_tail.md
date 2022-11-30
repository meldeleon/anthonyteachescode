## head or tail
- head taking the top number of lines,
- tail takes the bottom number of line.
  - `-f` will follow a file or `-F`, if contents get put into this file, it will show up. 
  - `-f` follows the same inode, but if you recreate the file (i.e. log rotation)it will not follow.
  - `-F` follows based on name.
