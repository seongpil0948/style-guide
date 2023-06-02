template <typename T>
struct Edge
{
    unsigned src;
    unsigned dst;
    T weight;

    inline bool operator<(const Edge<T> &e) const
    {
        return this->weight < e.weight;
    }
};

template <typename T>
class Graph
{
public:
    // N개의 정점으로 구성된 그래프
    Graph(unsigned N) : V(N) {}

    // 그래프의 정점 개수 반환
    auto vertices() const { return V; }

    // 전체 에지 리스트 반환
    auto &edges() const { return edge_list; }

    // 정점 v에서 나가는 모든 에지를 반환
    auto edges(unsigned v) const
    {
        vector<Edge<T>> edges_from_v;
        for (auto &e : edge_list)
        {
            if (e.src == v)
                edges_from_v.emplace_back(e);
        }

        return edges_from_v;
    }

    void add_edge(Edge<T> &&e)
    {
        // 에지 양 끝 정점 ID가 유효한지 검사
        if (e.src >= 1 && e.src <= V && e.dst >= 1 && e.dst <= V)
            edge_list.emplace_back(e); // 생성자를 내부에서 호출
        else
            cerr << "에러: 유효 범위를 벗어난 정점!" << endl;
    }

    // 표준 출력 스트림 지원
    template <typename U>
    friend ostream &operator<<(ostream &os, const Graph<U> &G);

private:
    unsigned V; // 정점 개수
    vector<Edge<T>> edge_list;
};

template <typename U>
ostream &operator<<(ostream &os, const Graph<U> &G)
{
    for (unsigned i = 1; i < G.vertices(); i++)
    {
        os << i << ":\t";

        auto edges = G.edges(i);
        for (auto &e : edges)
            os << "{" << e.dst << ": " << e.weight << "}, ";

        os << endl;
    }

    return os;
}
