class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        // use hashmap to create count 
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num: nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // use minHeap to store values 
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> 
            map.get(a) - map.get(b)
        );

        for (Map.Entry<Integer, Integer> entry: map.entrySet()){
            minHeap.add(entry.getKey());

            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }


        int[] res = new int[k];
        for(int i = 0; i < k; i++) {
            res[i] = minHeap.poll();
        }

        return res;
    }
}
