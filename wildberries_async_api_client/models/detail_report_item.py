from typing import *

from pydantic import BaseModel, Field


class DetailReportItem(BaseModel):
    """
    None model
    """

    realizationreport_id: Optional[int] = Field(alias="realizationreport_id", default=None)

    date_from: Optional[str] = Field(alias="date_from", default=None)

    date_to: Optional[str] = Field(alias="date_to", default=None)

    create_dt: Optional[str] = Field(alias="create_dt", default=None)

    currency_name: Optional[str] = Field(alias="currency_name", default=None)

    suppliercontract_code: Optional[Dict[str, Any]] = Field(alias="suppliercontract_code", default=None)

    rrd_id: Optional[int] = Field(alias="rrd_id", default=None)

    gi_id: Optional[int] = Field(alias="gi_id", default=None)

    subject_name: Optional[str] = Field(alias="subject_name", default=None)

    nm_id: Optional[int] = Field(alias="nm_id", default=None)

    brand_name: Optional[str] = Field(alias="brand_name", default=None)

    sa_name: Optional[str] = Field(alias="sa_name", default=None)

    ts_name: Optional[str] = Field(alias="ts_name", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

    doc_type_name: Optional[str] = Field(alias="doc_type_name", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    retail_price: Optional[float] = Field(alias="retail_price", default=None)

    retail_amount: Optional[float] = Field(alias="retail_amount", default=None)

    sale_percent: Optional[int] = Field(alias="sale_percent", default=None)

    commission_percent: Optional[float] = Field(alias="commission_percent", default=None)

    office_name: Optional[str] = Field(alias="office_name", default=None)

    supplier_oper_name: Optional[str] = Field(alias="supplier_oper_name", default=None)

    order_dt: Optional[str] = Field(alias="order_dt", default=None)

    sale_dt: Optional[str] = Field(alias="sale_dt", default=None)

    rr_dt: Optional[str] = Field(alias="rr_dt", default=None)

    shk_id: Optional[int] = Field(alias="shk_id", default=None)

    retail_price_withdisc_rub: Optional[float] = Field(alias="retail_price_withdisc_rub", default=None)

    delivery_amount: Optional[int] = Field(alias="delivery_amount", default=None)

    return_amount: Optional[int] = Field(alias="return_amount", default=None)

    delivery_rub: Optional[float] = Field(alias="delivery_rub", default=None)

    gi_box_type_name: Optional[str] = Field(alias="gi_box_type_name", default=None)

    product_discount_for_report: Optional[float] = Field(alias="product_discount_for_report", default=None)

    supplier_promo: Optional[float] = Field(alias="supplier_promo", default=None)

    rid: Optional[int] = Field(alias="rid", default=None)

    ppvz_spp_prc: Optional[float] = Field(alias="ppvz_spp_prc", default=None)

    ppvz_kvw_prc_base: Optional[float] = Field(alias="ppvz_kvw_prc_base", default=None)

    ppvz_kvw_prc: Optional[float] = Field(alias="ppvz_kvw_prc", default=None)

    sup_rating_prc_up: Optional[float] = Field(alias="sup_rating_prc_up", default=None)

    is_kgvp_v2: Optional[float] = Field(alias="is_kgvp_v2", default=None)

    ppvz_sales_commission: Optional[float] = Field(alias="ppvz_sales_commission", default=None)

    ppvz_for_pay: Optional[float] = Field(alias="ppvz_for_pay", default=None)

    ppvz_reward: Optional[float] = Field(alias="ppvz_reward", default=None)

    acquiring_fee: Optional[float] = Field(alias="acquiring_fee", default=None)

    acquiring_bank: Optional[str] = Field(alias="acquiring_bank", default=None)

    ppvz_vw: Optional[float] = Field(alias="ppvz_vw", default=None)

    ppvz_vw_nds: Optional[float] = Field(alias="ppvz_vw_nds", default=None)

    ppvz_office_id: Optional[int] = Field(alias="ppvz_office_id", default=None)

    ppvz_office_name: Optional[str] = Field(alias="ppvz_office_name", default=None)

    ppvz_supplier_id: Optional[int] = Field(alias="ppvz_supplier_id", default=None)

    ppvz_supplier_name: Optional[str] = Field(alias="ppvz_supplier_name", default=None)

    ppvz_inn: Optional[str] = Field(alias="ppvz_inn", default=None)

    declaration_number: Optional[str] = Field(alias="declaration_number", default=None)

    bonus_type_name: Optional[str] = Field(alias="bonus_type_name", default=None)

    sticker_id: Optional[str] = Field(alias="sticker_id", default=None)

    site_country: Optional[str] = Field(alias="site_country", default=None)

    penalty: Optional[float] = Field(alias="penalty", default=None)

    additional_payment: Optional[float] = Field(alias="additional_payment", default=None)

    rebill_logistic_cost: Optional[float] = Field(alias="rebill_logistic_cost", default=None)

    rebill_logistic_org: Optional[str] = Field(alias="rebill_logistic_org", default=None)

    kiz: Optional[str] = Field(alias="kiz", default=None)

    storage_fee: Optional[float] = Field(alias="storage_fee", default=None)

    deduction: Optional[float] = Field(alias="deduction", default=None)

    acceptance: Optional[float] = Field(alias="acceptance", default=None)

    srid: Optional[str] = Field(alias="srid", default=None)

    report_type: Optional[int] = Field(alias="report_type", default=None)
