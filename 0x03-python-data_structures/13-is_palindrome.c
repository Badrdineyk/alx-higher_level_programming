#include "lists.h"

/**
 * reverse_list - Reverses a singly-linked list.
 * @head: Pointer to the starting node of the list to reverse.
 *
 * Return: Pointer to the head of the reversed list.
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next_node, *prev = NULL;

	while (current)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	size_t size = 0, i;
	listint_t *fast, *prev, *mid_node;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	fast = *head;
	while (fast)
	{
		size++;
		fast = fast->next;
	}
	fast = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		fast = fast->next;
	if ((size % 2) == 0 && fast->n != fast->next->n)
		return (0);
	fast = fast->next->next;
	prev = reverse_list(&fast);
	mid_node = prev;
	fast = *head;
	while (prev)
	{
		if (fast->n != prev->n)
			return (0);
		fast = fast->next;
		prev = prev->next;
	}
	reverse_list(&mid_node);
	return (1);
}
