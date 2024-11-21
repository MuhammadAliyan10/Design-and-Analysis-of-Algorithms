# AVL Tree Insertion Example

## Introduction to AVL Tree

An **AVL Tree** is a self-balancing binary search tree where the difference in heights of the left and right subtrees of any node is at most 1. The tree rebalances itself by performing rotations whenever necessary to ensure that the height difference between the left and right subtrees (balance factor) is within the acceptable range of -1, 0, or 1.

---

## Insert Values Example:

Let's walk through the process of inserting the following values into an AVL tree:

### Step-by-Step Insertion:

1. **Insert 25**:

   - The tree is empty, so `25` becomes the root.

2. **Insert 29**:

- `29` is greater than `25`, so it goes to the right of `25`.

3. **Insert 30**:

- `30` is greater than both `25` and `29`, so it becomes the right child of `29`.
- After this insertion, the tree becomes unbalanced (Right-Right case), so we perform a **Left Rotation** on `25`.

**Left Rotation on node 25**:

4. **Insert 15**:

- `15` is less than `29` but greater than `25`, so it goes to the right of `25`.

  29
  / \
  25 30
  \
   15

5. **Insert 12**:

- `12` is less than `29`, `25`, and `15`, so it becomes the left child of `15`.

  29
  / \
  25 30
  \
   15
  /

6. **Insert 14**:

- `14` is less than `29`, greater than `12`, and less than `15`, so it becomes the right child of `12`.
- The tree becomes unbalanced at node `25` (Left-Right case), so we perform a **Left Rotation** on `12`, followed by a **Right Rotation** on `25`.

**Left Rotation on node 12**:
29
/ \
25 30
\
 15
/

After the rotation, the tree looks like:

29
/ \
15 30

7. **Insert 10**:

- `10` is less than `29`, `15`, and `12`, so it becomes the left child of `12`.

  29
  / \
  15 30

8. **Insert 9**:

- `9` is less than all nodes, so it becomes the left child of `10`.

  29
  / \
  15 30

9. **Insert 45**:

- `45` is greater than all the nodes, so it becomes the right child of `30`.

  29
  / \
  15 30

10. **Insert 47**:

- `47` is greater than all the nodes, so it becomes the right child of `45`.

  29
  / \
  15 30

---

## Final AVL Tree:

The final AVL tree after inserting all the values is as follows:

29
/ \
15 30

### Tree Visualization with Branches:

Here is the visualization using `/\` for left children and `\/` for right children:

29
/\  
15 30

---

## Explanation:

- **Node Balancing**: After each insertion, we checked for the balance of the tree, and whenever the balance factor went outside the range of `[-1, 1]`, we performed rotations to ensure the AVL property.
- **Rotations**:
  - **Left Rotation**: Performed when a right-heavy subtree causes an imbalance.
  - **Right Rotation**: Performed when a left-heavy subtree causes an imbalance.
  - **Left-Right Rotation**: Performed when a left child has a right-heavy subtree.
  - **Right-Left Rotation**: Performed when a right child has a left-heavy subtree.

By maintaining balance, the AVL tree ensures that operations like insertion, deletion, and searching can be done efficiently in `O(log n)` time.

---

## Conclusion:

This example demonstrates how the AVL tree automatically rebalances itself during insertion to maintain the properties of a balanced binary search tree. By using rotations, the AVL tree ensures that the height difference between the left and right subtrees of any node is at most 1, guaranteeing efficient operations.
