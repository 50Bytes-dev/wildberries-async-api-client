from enum import Enum


class RefundActionType(str, Enum):

    SELLERREQUESTREFUND = "sellerRequestRefund"
    SELLERREJECTREFUND = "sellerRejectRefund"
    SELLERACCEPTFULLREFUND = "sellerAcceptFullRefund"
    SELLERACCEPTREFUNDINOFFICE = "sellerAcceptRefundInOffice"
