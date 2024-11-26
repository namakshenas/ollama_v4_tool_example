import ollama

def knapsack(utilities: list[int], weights: list[int], capacity: int) -> int:
    """
    Solve the 0/1 Knapsack problem using a functional and recursive approach.

    Args:
        utilities (list[int]): A list of integers representing the values of the items.
        weights (list[int]): A list of integers representing the weights of the items.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        int: The maximum value that can be obtained within the given weight capacity.
    """
    return (lambda dp: dp(dp, capacity, len(utilities)))(
        lambda f, c, i: 0
        if c == 0 or i == 0
        else f(f, c, i - 1)
        if weights[i - 1] > c
        else max(f(f, c, i - 1), utilities[i - 1] + f(f, c - weights[i - 1], i - 1))
    )

response = ollama.chat(
    model='llama3.2',
    messages=[
        {
            "role": "user",
            "content": """
             I have a list of items with utilites [60, 100, 120], 
             weights [10, 20, 30], and a knapsack with a weight capacity of 50. Can you help 
             me find the maximum utility that can be obtained within the given weight capacity?
             """,
        }
    ],
    tools=[knapsack]
)

print(response['message']['content'])
