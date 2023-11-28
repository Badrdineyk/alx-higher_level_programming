#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: The head of the linked list.
 * @number: Number to insert.
 *
 * Return: Pointer to the new node. Or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head, *n_node;

	n_node = malloc(sizeof(listint_t));
	if (n_node == NULL)
		return (NULL);
	n_node->n = number;
	if (current_node == NULL || current_node->n >= number)
	{
		n_node->next = current_node;
		*head = n_node;
		return (n_node);
	}
	while (current_node && current_node->next && current_node->next->n < number)
		current_node = current_node->next;
	n_node->next = current_node->next;
	current_node->next = n_node;
	return (n_node);
}
