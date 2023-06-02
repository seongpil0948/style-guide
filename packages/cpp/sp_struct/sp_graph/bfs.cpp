#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <queue>

using namespace std;
template <typename T>
struct Edge
{
    unsigned src;
    unsigned dst;
    T weight;
};

template <typename T>
struct Graph
{
public:
    vector<Edge> edge_list;

    // consist N Vertices Graph
    Graph(unsigned N) : V(N)
    {
    }
    // num of vertice
    auto vertices() const { return V; }

    // all edges
    auto &edges() const { return edge_list; }
};