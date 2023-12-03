/*
 쓰레드 인자 전달
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 5

void *hello_thread(void *arg)
{
    int thread_num = *((int *)arg); 
    printf(" Thread %d: Hi, I'm Thread %d!\n", thread_num, thread_num);
    return arg;
}

int main()
{
    pthread_t pid[NUM_THREADS];
    int i, status;
    int thread_args[NUM_THREADS]; 

    // pthread create
    for (i = 0; i < NUM_THREADS; i++)
    {
        thread_args[i] = i;
        status = pthread_create(&pid[i], NULL, hello_thread, (void *)&thread_args[i]);
        if (status != 0)
        {
            fprintf(stderr, "Create thread %d: %d", i, status);
            exit(1);
        }
    }
    pthread_exit(NULL);
}

