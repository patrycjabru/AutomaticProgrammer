grammar cargobot;

start: block section section section;
section: separator block | separator;
block: block block | action | conditional_statement;
conditional_statement: condition conditional_action;
conditional_action: LEFT_ARROW | RIGHT_ARROW | DOWN_ARROW | PROGRAM1 | PROGRAM2 | PROGRAM3 | PROGRAM4;
action: LEFT_ARROW | RIGHT_ARROW | DOWN_ARROW | PROGRAM1 | PROGRAM2 | PROGRAM3 | PROGRAM4;
condition: ALL | EMPTY | COLOR1 | COLOR2 | COLOR3 | COLOR4;
separator: SEPARATOR;

SEPARATOR: 'separator';
ALL: 'all';
EMPTY: 'empty';
COLOR1: 'color1';
COLOR2: 'color2';
COLOR3: 'color3';
COLOR4: 'color4';
LEFT_ARROW: 'left_arrow';
RIGHT_ARROW: 'right_arrow';
DOWN_ARROW: 'down_arrow';
PROGRAM1: 'program1';
PROGRAM2: 'program2';
PROGRAM3: 'program3';
PROGRAM4: 'program4';

WS: . -> skip;
