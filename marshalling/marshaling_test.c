#include <stdio.h>
#include <arpa/inet.h>

int main() {
    int number = 12345;

    // Marshaling: Convert host byte order to network byte order
    int32_t marshaled = htonl(number);

    // Transmit `marshaled` over a network...

    // On the receiving end:
    int32_t received = marshaled;

    // Unmarshaling: Convert network byte order back to host byte order
    int32_t unmarshaled = ntohl(received);
    printf("Unmarshaled number: %d\n", unmarshaled);

    return 0;
}
