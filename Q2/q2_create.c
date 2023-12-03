/*
쓰레드 생성 함수
*/

#include <stdio.h>
#include <pthread.h>


void *hello_thread(void *arg)
{
	printf(" Thread : Hi I'm Thread! \n");
	return arg;
}

void *bye_thread(void *arg)
{
	printf(" Thread : Bye \n");
	return arg;
}



int main()
{

	pthread_t pid;
	int status;
	
	// thread create
	status = pthread_create(&pid, NULL, hello_thread, NULL);
	status = pthread_create(&pid, NULL, bye_thread, NULL);
	
	if (status != 0)
		perror ("Create thread");
	pthread_exit (NULL);

	return 0;
}
