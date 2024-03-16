// solution to travelling salesman problem
// given: weighted adjacency matrix, number of cities, starting index

import { MinPriorityQueue } from "@datastructures-js/priority-queue";

function solution(graph, n, start) {
  let minDist = Infinity;
  const endMask = (1 << n) - 1;

  const dp = new Array(1 << n)
    .fill(null)
    .map(() => new Array(n).fill(Infinity));
  dp[1 << start][start] = 0;

  const queue = new MinPriorityQueue((obj) => obj.value);
  queue.push({
    value: 0,
    curr: start,
    mask: 1 << start,
  });

  while (!queue.isEmpty()) {
    const { value, mask, curr } = queue.pop();
    if (value >= minDist) return minDist;

    if (mask === endMask) {
      minDist = Math.min(minDist, value + graph[curr][start]);
    } else {
      for (let next = 0; next < n; next++) {
        if ((mask & (1 << next)) === 0) {
          const nextMask = mask | (1 << next);
          const nextDist = dp[mask][curr] + graph[curr][next];
          if (nextDist < dp[nextMask][next]) {
            dp[nextMask][next] = nextDist;
            queue.push({ value: nextDist, mask: nextMask, curr: next });
          }
        }
      }
    }
  }
}
