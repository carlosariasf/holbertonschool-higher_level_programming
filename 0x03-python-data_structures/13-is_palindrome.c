#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - check if linked list is palindrome
 * @head: list to check
 * Return: 1 if is a palindrome 0 if not
 *
**/
int is_palindrome(listint_t **head)
{
    long int list[100024];
	long int count = 0, count2 = 1, final = 0, i;
	
    if (head == NULL)
        return (0);
    if ((*head) != NULL)
	{
		while ((*head)->next != NULL)
		{
            list[count] = (*head)->n;
			(*head) = (*head)->next;
            count++;
		}
        list[count] = (*head)->n;
        count++;
		if (count % 2 == 0)
		{
			count2 = count / 2;
			for (i = 0; i < count2; i++)
			{
				if (list[i] == list[count-1])
					final++;
                count--;
			}
			if (final == count2)
				return (1);
			else
				return (0);
		}
		else
			return (0);
	}
    return (1);
}
