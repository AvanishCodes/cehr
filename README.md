# CEHR

### Diagram

classDiagram
direction BT
class node12
class node18
class node20
class node23
class node25
class node17
class node24
class node19
class node8
class node0
class node6
class node14
class node11
class node16
class node4
class node15
class node21
class node22
class node5
class node9
class node26
class node10
class object
class node3
class node1
class node13
class node2

node12 "0..*" --* "1" node18
node12 "0..*" --* "1" node23
node12 "1" --* "1" node8
node18 "0..*" --* "1" node20
node18 "0..*" --* "1" node23
node18 "1" --* "1" node8
node20 "1" --* "1" node8
node23 "0..*" --* "1" node20
node23 "1" --* "1" node8
node25 "0..*" --* "0..*" node17
node25 "1" --* "1" node8
node17 "0..*" --* "1" node19
node17 "1" --* "1" node8
node24 "0..*" --* "0..*" node25
node24 "0..*" --* "0..*" node17
node19 "1" --* "1" node8
node8 "1" --* "1" object
node0 "1" --* "1" node8
node6 "1" --* "1" node24
node6 "1" --* "1" node8
node6 "0..*" --* "1" node16
node6 "0..*" --* "1" node15
node14 "0..*" --* "1" node12
node14 "1" --* "1" node8
node11 "1" --* "1" node8
node11 "0..*" --* "1" node6
node11 "0..*" --* "1" node14
node16 "1" --* "1" node8
node16 "0..*" --* "1" node15
node4 "1" --* "1" node8
node4 "0..*" --* "1" node6
node4 "0..*" --* "1" node21
node15 "1" --* "1" node8
node21 "0..*" --* "1" node12
node21 "1" --* "1" node8
node21 "0..*" --* "1" node0
node22 "1" --* "1" node8
node22 "0..*" --* "1" node5
node22 "0..*" --* "1" node10
node5 "1" --* "1" node8
node9 "1" --* "1" node8
node9 "0..*" --* "1" node26
node26 "0..*" --* "1" node12
node26 "1" --* "1" node8
node10 "1" --* "1" node8
node3 "1" --* "1" node24
node3 "1" --* "1" node8
node1 "1" --* "1" node8
node13 "1" --* "1" node8
node13 "0..*" --* "1" node9
node13 "0..*" --* "1" node1
node13 "0..*" --* "1" node2
node2 "0..*" --* "1" node12
node2 "1" --* "1" node8
node2 "0..*" --* "1" node6
node2 "0..*" --* "1" node3 
