import java.util.PriorityQueue;

public class Solution {
    // 参考: https://github.com/ZXZxin/ZXBlog/blob/master/%E5%88%B7%E9%A2%98/Other/%E5%89%91%E6%8C%87Offer/%E5%89%91%E6%8C%87Offer%20-%2063%20-%20%E6%95%B0%E6%8D%AE%E6%B5%81%E4%B8%AD%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.md
    //堆顶最小，但是存的是最大的 n/2个元素
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    //堆顶最大，但是存的是最小的 n/2个元素
    private PriorityQueue<Integer> maxHeap = new PriorityQueue<>((o1, o2) -> o2 - o1);

    public void Insert(Integer num) {
        if(maxHeap.isEmpty() || num <= maxHeap.peek()){
            maxHeap.add(num);
        }else{
            minHeap.add(num);
        }
        if(minHeap.size() - maxHeap.size() > 1)
            maxHeap.add(minHeap.poll());
        else if(maxHeap.size() - minHeap.size() > 1){
            minHeap.add(maxHeap.poll());
        }
    }

    public Double GetMedian() {
        if(minHeap.size() > maxHeap.size())
            return 1.0 * minHeap.peek();
        else if(maxHeap.size() > minHeap.size())
            return 1.0 * maxHeap.peek();
        else
            return 1.0 * (minHeap.peek() + maxHeap.peek())/2;
    }

}