#include "binTree.hpp"

int main() {
    auto tree = binTree::createBinTree("CEO");
    tree.insert("CEO", "부사장");
    tree.insert("부사장", "CTO");
    tree.insert("부사장", "마케팅부장");
    tree.insert("부사장", "경리");
    tree.insert("CTO", "앱개발팀장");
    tree.insert("CTO", "보안팀장");
    tree.insert("마케팅부장", "물류팀장");
    tree.insert("마케팅부장", "홍보팀장");
    tree.preOrder(tree.root);
    return 0;
}



 


