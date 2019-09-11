# pom-parser
Simple python script to check for duplicate or redundant dependencies in pom files.

Put a copy of your pom files in the same directory as the pom-parser.py for convenience.

For a list of commands, run: <br>
python pom-parser.py --help

Example comparing two pom-files for dependency collisions: <br>
python pom-parser.py check-collisions pom_1.xml pom_2.xml

Note: <br>
Make sure the first argument is the file you want to compare with and the second file is then the one which is checked for collisions.
