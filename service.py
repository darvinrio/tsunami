from connecpy.exceptions import InvalidArgument
from connecpy.context import ServiceContext

from proto.aloha_pb2 import NullAddressRequest, NullAddressResponse


class AlohaEthereumService:
    async def GetNullAddress(
        self, request: NullAddressRequest, context: ServiceContext
    ) -> NullAddressResponse:
        """
        This method is used to get the null address for a given address.
        """

        return NullAddressResponse(
            address="0x0000000000000000000000000000000000000000",
            checksummed="0x0000000000000000000000000000000000000000",
        )

    async def ChecksumAddress(
        self, request: NullAddressRequest, context: ServiceContext
    ) -> NullAddressResponse:
        """
        This method is used to get the checksummed address for a given address.
        """

        if not request.address:
            raise InvalidArgument("Address is required")

        return NullAddressResponse(address=request.address, checksummed=request.address)
