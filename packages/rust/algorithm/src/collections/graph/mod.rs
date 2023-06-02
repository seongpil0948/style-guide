mod dfs;

// /// Represents a union of disjoint sets. Each set's elements are arranged in a
// /// tree, whose root is the set's representative.
// pub struct DisjointSets {
//     parent: Vec<usize>,
// }

// impl DisjointSets {
//     /// Initializes disjoint sets containing one element each.
//     pub fn new(size: usize) -> Self {
//         Self {
//             parent: (0..size).collect(),
//         }
//     }

//     /// Finds the set's representative. Do path compression along the way to make
//     /// future queries faster.
//     pub fn find(&mut self, u: usize) -> usize {
//         let pu = self.parent[u];
//         if pu != u {
//             self.parent[u] = self.find(pu);
//         }
//         self.parent[u]
//     }

//     /// Merges the sets containing u and v into a single set containing their
//     /// union. Returns true if u and v were previously in different sets.
//     pub fn merge(&mut self, u: usize, v: usize) -> bool {
//         let (pu, pv) = (self.find(u), self.find(v));
//         self.parent[pu] = pv;
//         pu != pv
//     }
// }

/// A compact graph representation. Edges are numbered in order of insertion.
/// Each adjacency list consists of all edges pointing out from a given vertex.
#[derive(Debug, Clone)]
pub struct Graph {
    /// Maps a vertex id to the first edge in its adjacency list.
    /// /// Maps a vertex id to the first edge in its adjacency list.
    first: Vec<Option<usize>>,
    /// Maps an edge id to the next edge in the same adjacency list.
    next: Vec<Option<usize>>,
    /// Maps an edge id to the vertex that it points to.
    last: Vec<usize>,
}

impl Graph {
    /// init Graph for Reduce
    /// vmax: num of vertex, amax: num of Arcs
    pub fn new(vmax: usize, amax: usize) -> Self {
        Self {
            // from vertext
            // 각 인덱스는 arc 개수를 나타낸다
            first: vec![None; vmax],
            // next vertext ( linked list )
            /// Maps an edge id to the next edge in the same adjacency list.
            next: Vec::with_capacity(amax),
            // to vertext
            /// Maps an edge id to the vertex that it points to.
            last: Vec::with_capacity(amax),
        }
    }
    /// Return Number of Vertices
    pub fn num_v(&self) -> usize {
        self.first.len()
    }
    /// Return Number of Arcs
    pub fn num_arcs(&self) -> usize {
        self.last.len()
    }

    // direct arc from u to v
    pub fn add_arc(&mut self, u: usize, v: usize) {
        self.next.push(self.first[u]);
        self.first[u] = Some(self.num_arcs());
        self.last.push(v)
    }

    /// all arcs are added via this func
    /// Adjacency matrix for undirected graph is always symmetric(even). 
    pub fn add_undirected_arc(&mut self, u: usize, v: usize) {
        self.add_arc(u, v);
        self.add_arc(v, u);
    }

    /// 2-SAT(2-SATisfiability)
    /// https://sevity.tistory.com/152
    /// If we think of each even-numbered vertex as a variable, and its
    /// odd-numbered successor as its negation, then we can build the
    /// implication graph corresponding to any 2-CNF formula.
    /// 짝수 번호의 각 정점을 변수로, 홀수 번호의 후속 정점을 부정으로 생각하면
    ///  2-CNF 공식에 해당하는 함축 그래프를 작성할 수 있습니다.
    /// Note that u||v == !u -> v == !v -> u.///
    pub fn add_two_sat_clause(&mut self, u: usize, v: usize) {
        // 짝수 일경우에 마지막 비트가 0 이기 때문에 XOR 로서 마지막 비트가 1이 되며 값이 1 올라간다
        // 홀수 '' 1 이기 때문에 0 이 된다, 값이 1 내려간다.
        self.add_arc(u ^ 1, v);
        self.add_arc(v ^ 1, u);
    }
    /// Gets vertex u's adjacency list.
    /// edge 하나로 갈수 있는 vertexes
    pub fn adj_list(&self, u: usize) -> AdjListIterator {
        AdjListIterator {
            graph: self,
            next_e: self.first[u],
        }
    }
}

/// Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph
/// The size of the array is equal to the number of vertices.
/// An entry array[i] represents the list of vertices adjacent to the ith vertex.
pub struct AdjListIterator<'a> {
    graph: &'a Graph,
    next_e: Option<usize>,
}

impl<'a> Iterator for AdjListIterator<'a> {
    type Item = (usize, usize);

    /// Produces an outgoing edge and vertex.
    fn next(&mut self) -> Option<Self::Item> {
        self.next_e.map(|e| {
            let v = self.graph.last[e];
            self.next_e = self.graph.next[e];
            (e, v)
        })
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_adj_list() {
        let mut graph = Graph::new(5, 6);
        graph.add_arc(2, 3);
        graph.add_arc(2, 4);
        graph.add_arc(4, 1);
        graph.add_arc(1, 2);
        graph.add_undirected_arc(0, 2);

        let adj = graph.adj_list(2).collect::<Vec<_>>();

        assert_eq!(adj, vec![(5, 0), (1, 4), (0, 3)]);
        for (e, v) in adj {
            assert_eq!(v, graph.last[e]);
        }
    }
}
