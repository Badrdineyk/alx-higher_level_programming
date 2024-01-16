#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *p;

	node = *head;
	p = malloc(sizeof(listint_t));
	if (p == NULL)
		return (NULL);
	p->n = number;

	if (node == NULL || node->n >= number)
	{
		p->next = node;
		*head = p;
		return (p);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	p->next = node->next;
	node->next = p;

	return (p);
}
