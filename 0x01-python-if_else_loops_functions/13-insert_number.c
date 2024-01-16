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
	listint_t *node, *p, *f;

	p = *head;
	f = (*head)->next;

	while (f->next)
	{
		if (p->n < number && f->n > number)
		{
			node = malloc(sizeof(listint_t));
			if (node == NULL)
				return (NULL);
			node->n = number;
			node->next = f;
			p->next = node;
			return (node);
		}
		p = p->next;
		f = f->next;
	}

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	f->next = node;
	node->next = NULL;
	return (node);
}
