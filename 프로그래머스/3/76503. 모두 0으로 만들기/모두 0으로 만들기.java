import java.util.*;

class Solution {
    public long solution(int[] a, int[][] edges) {
        return new Prob3_Compact(a, edges).solve();
    }
}
class Prob3_Compact
{
	static class Node
	{
		ArrayList<Integer> adjacentList = new ArrayList<>();
	}

	static Node[] nodes;
	static long answer = 0;
	static long[] weight;

	public Prob3_Compact(int[] a, int[][] edges)
	{
		weight = Arrays.stream(a).asLongStream().toArray();
		nodes = new Node[a.length];
		for (int i = 0; i < nodes.length; i++) nodes[i] = new Node();

		for (int[] edge : edges)
		{
			nodes[edge[0]].adjacentList.add(edge[1]);
			nodes[edge[1]].adjacentList.add(edge[0]);
		}
	}

	public static long solve()
	{
		if (Arrays.stream(weight).sum() != 0) return -1;
		dfs(0, 0);
		return answer;
	}

	private static void dfs(int current, int parent)
	{
		for (int node : nodes[current].adjacentList)
			if (node != parent) dfs(node, current);

		weight[parent] += weight[current];
		answer += Math.abs(weight[current]);
	}
}