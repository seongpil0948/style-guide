#ifndef bin_tree_hpp
#define bin_tree_hpp

#include <queue>
#include <stdio.h>
#include <iostream>

struct node {
    std::string data;
    node* first;
    node* second;
};

struct binTree {
    node* root;
    
    static binTree createBinTree(const std::string& data) {
        binTree tree;
        tree.root = new node {data, NULL, NULL};
        return tree;
    }
    // first check root node
    // find left subtree if not exist in root
    // find right sub if not at all
    static node* find(node* root, const std::string& val)
    {
        if (root == NULL) return NULL;
        
        if (root->data == val) return root;
        
        auto firstFound = binTree::find(root->first, val);
        
        if (firstFound != NULL) return firstFound;
        
        return binTree::find(root->second, val);
    }
    
    bool insert (const std::string& parentVal, const std::string& newVal) {
        auto parentNode = binTree::find(root, parentVal);
        
        if (!parentNode) {
            std::cout << parentVal << "을 찾을 수 없습니다" << std::endl;
            return false;
        }
        if (parentNode->first && parentNode->second) {
            std::cout << parentNode << "아래에 " << newVal << "을 추가 할 수 없습니다" << std::endl;
            return false;
        }
        
        if (!parentNode->first) {
            parentNode->first = new node {newVal, NULL, NULL};
        } else {
            parentNode->second = new node{newVal, NULL, NULL};
        }
        std::cout << parentNode << " 아래에 " << newVal << "을 추가 했습니다" << std::endl;
        return true;
    }
    
    static void preOrder(node* start) {
        if (!start) return;
        
        std::cout << start->data << ", ";
        preOrder(start->first);
        preOrder(start->second);
    }
};
#endif /* bin_tree_hpp */
