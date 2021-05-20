# -*- coding: utf-8 -*-
import requests
import json

headerscookies0 = {
    "Cookie": "language=cn; _ga=GA1.2.212260452.1596423198; _ntes_nnid=87123d721804542893a0b50beafcbf21,1596525450978; NTES_SESS=5TaEBtnzQQ1xrzoLLCgV1TycdAhT0JVHmgYN9CNjWFF0Wh3VWELSHa7UL3yIJ8VB9O_CQY6XRufWBaAUrHJG3fsFK3s1cFPx8U9yiudEytCRUbTWygIcGnazqYCeTY.KDjQksZZD0.hUo50EzwqTOQ4mNr1OLR4MwHYtvota2QcV8YtA60qrtWX_xQwF_osJ2nwp2tjWXeh.a; NTES_PASSPORT=eV8.Vgad0LRxFyUnG2YkXdw.BpSf4R8bfnMCRZr8v7nmv4jcvh2dqAZt2jgOxfc18fYxE._Rbat2b1WuNijg7r.Z5sB6YfymvQk7AGZ5RihjSoSicCa4YGr_KYJY..UFdn9D8.N.g4.BLR_dTcpS9KVuoQpicnUgaM7CuVtnCUrHQk3Y6EG4U5AlBk59mGsAj; S_INFO=1597198700|0|2&70##|montest85; P_INFO=montest85@163.com|1597198700|1|hongcai|00&99|bej&1597030409&hongcai#bej&null#10#0#0|&0|hongcai|montest85@163.com"
}

headerscookies1 = {
    "Cookie": "language=cn; NTES_SESS=VB_LoLOHhZNOvD4L8HMyo69aaQ7k8BDVCHJg4qgFu88hcDZbfciZJUX07deCD6mI41z58hVQMfrcIxi0ksDUdow8NdwOR8Tn604e3X95eYqqW.jpSLELDAan2vP8i1q38FVQwAAfjlWkXRt.BDbUgr0yyca_UzzTp7ASkbGO7ib6prRovmy1KyyabC_SYiij2; NTES_PASSPORT=MZZXyCqCLPmXIcmsPpasn1np.5sXEFSDZDGgm7C9WtDxeJ2XDeA2YGuUL3yIJ8VB9jDRefVciN_WrB51bx3ytCv7lcK408kTW_qtaZ7lmxE3f6fxVgYh0ZkAr2qUEeLxhHuiXua5HG6WgDlyJ2h8mdPx9UmPx7JLPEarsGuXydnIX; S_INFO=1597199468|0|2&10##|montest86; P_INFO=montest86@163.com|1597199468|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||montest86@163.com"
}

headerscookies2 = {
    "Cookie": "language=cn; NTES_SESS=cHt290Db8Rq51tiVBnHH.GEHb8A_uzsoazHpbfJHLvrgsnGNSs0Gxt5r55g4gdnaerEcdA11j7IRSFM4SwTAiIprncdXUbEaWgDbWbn6ndjEsw.xHqUVq2w..M6VCFscc9bxfOJMDSiKxhl0PrSqC1JRlTLZJ3HDOlIB5U97T_UXob0twZQEXLKub3F1kCy8v; NTES_PASSPORT=pfTuWRqV1oq0WhW6jyNq7diJ9nb5tMaKWKJeKxiyZfjCIZQ.AImQ2cSWSSljlUZwKdNmVZxGaajqgdWKQbwkiOT_eM1en1iy.bEJZaluIpdlPpDxZ1rznhPIChn536cHLAkt1CdYmmUF1PvjwGsfagYJzIEeLXOLtUdEFO6sHE_u_UTMCuXfL02k0; S_INFO=1597199664|0|2&10##|ad_jztest507; P_INFO=ad_jztest507@163.com|1597199664|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest507@163.com"
}

headerscookies3 = {
    "Cookie": "language=cn; NTES_SESS=fdnigig0o2gJ3oDirAmheVXjHQmS62ZF6QnLYqInER0xSrvakSKvOlT0TTxcxyr1DxRI5ftnjSq5kg.ckz4uXAL0rfytpYP1mxCYmYrsryNPSzwOn3p83hzww.s8igSffeYOqUI.CkX7OV2K90k3iGS8rzyUJMHLmbPyFGv2.3DELYbGn5LxkGWJ5J1HhrkEo; NTES_PASSPORT=KTMdZgVz_q8LsL6WbEFsNaONuVRvo2MitNDcNn3eAoFqCAVliCMVZRzuzzBFB0A2NKz2Nm_1Dn28H9uNVy2Q3rGPctOcSO3ely5DAxBXCK9BTKfnAOkhSWUj8DE0XEfe9wLsFB75v_87jaROX1IUQEuEtYQJBkxSrcB0gW0rYrL18nzWwLiK7VHQj; S_INFO=1597199761|0|2&10##|ad_jztest506; P_INFO=ad_jztest506@163.com|1597199761|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest506@163.com"
}

headerscookies4 = {
    "Cookie": "language=cn; NTES_SESS=V8WYypVI6AOEgVIBRmAgwmIFa9aKR7bnGoeur8jeMWCycDZbfciZJUlCllyhySDYQ2odET8fgRWEfdGhfR2axNuCDVSOAr.Y5yFr5rD4DS3.cRvJeHAPHLRvvG4PgdcVVzrJ8IjGFfxXJEpiwCfHgBjHe9s.wIOLUV6rCyX2DvSX_sDbTVtSQxzt4ALuWUZP0; NTES_PASSPORT=vhpraTSp1.M1Z32o5xBtqIrg9ja6IOC9GpYypaAb2D0IB2k6ZBVkwenhnn.0.G2spwbnA8lWOrSjN3hpkXsrA1Pqym5yx5Ab6XoY27.WBv3._vJa25OSxz1t5btp5zhDcZd9kRzaA6Ye8L49iAq22GVGl0kHQxtiObTGONCtbDDWZXViwgUlLmNrU; S_INFO=1597199918|0|2&10##|ad_jztest505; P_INFO=ad_jztest505@163.com|1597199918|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest505@163.com"

}

headerscookies5 = {
    "Cookie": "language=cn; NTES_SESS=tcaR_0AOrDo_Oig_9PY0HmB_6FoYtnlan1LyVl6LJbPR7E3c5793oFCPCCRXRWEfMuc_tvPAgreQ5vjX5aiSzsyPEtWQdVIfrR.VrVEKEW4I7aNoL2dU2xaNNjKUwv7ttuVol_6j.5zeoOg9AP52wqYoyoNjScKO1EoUHyAA8qHTdt3QIyKV7LCzcUl9h0zwq; NTES_PASSPORT=CIZFynmQ321PIL1RonI1YQXYrU_Hli5kGqz2q98wjWoVQjLOFQaL0ZvNvvrorDjUqRIyGa5vFKRJP.NqLsUR8eYM2xy24y8wOsXzjdrgQC.rtCh9jycp4KONt5J8mt.v5ZoSBPIE4metTVq7viDf1wv6fR3oaZ6oD73uZVHTiNoiQET_KpKtCw6Rf; S_INFO=1597200012|0|2&10##|ad_jztest504; P_INFO=ad_jztest504@163.com|1597200012|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest504@163.com"
}

headerscookies6 = {
    "Cookie": "language=cn; NTES_SESS=LGbEh3qCBz3xbnzzTq4W2abtbpVkWXm0EWwNeEfwaKQs2z0Hh2F0SJOQOOsps4znRXfoxD5.kSVbh6YphZU3dqNQzL4yje1nXsoeXezlz4812ZBSwPjMPAZBBYlM_62LLveSEkfYohdgg0GQilHDhf.oaLEI1uAw476HS3XKRfUVsUhELKR9Ym7P3NwRfaWBG; NTES_PASSPORT=M7z3mQAxEfYgydKW5uVDdwLKiFLi2gupBtNFtIOj5Hbxa5dR1a4dE8qTqqLbLu5ot.r9G02KLl8zJkTtd0o3OAhSFvZFCZOjR0wN5BLGaMkLzMgI5Zi_CPVyRKsBluGcsCagyT5BKtEDZaWQ3q83bzQ2zRsVmY3C_zvP.9x47Rc1ER11RxRCcPJ3X; S_INFO=1597200298|0|2&10##|ad_jztest503; P_INFO=ad_jztest503@163.com|1597200298|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest503@163.com"
}

headerscookies7 = {
    "Cookie": "language=cn; NTES_SESS=41SWbEo91KLOw_.A7yQT_En7AAwEc36NXw8U3cy8pGnF6H1js6r1gX7n77FTF_HN93pKz1wnHiRdsQuTs.5ICJUnH4_iO3LNZFe3Z3HmH_kL6.Mg8fOhfl.MMumhDQ644P3gcxyuesC001EnBmjbsy_F70EA.0HSP_uLnNwlBgYfHDCgIibzqSRe78rJ4QxSy; NTES_PASSPORT=tNRX2k1ANOD9bCpeYTRzPECDo1vWK8pQTYg8YCrF1synx19LOxv956_G__7y7X1EYW5EOgiF3ixyDQGY9jEdriWz8pA8qArFLj2g1I7UxtQ7htHC1A3PqTLFv4V1VhJ3sowduZdHNNAfYG3AAAxO3dFPwJzBjQf0OZ37SA39EH7Nneb3A8EboCMdb; S_INFO=1597200427|0|2&10##|ad_jztest502; P_INFO=ad_jztest502@163.com|1597200427|1|hongcai|00&99|bej&1594709393&hongcai#bej&null#10#0#0|&0||ad_jztest502@163.com"
}

headerscookies8 = {
    "Cookie": "language=cn; NTES_SESS=122iNAu6ZfGx4mpoLB.Dkwh2uo6gh3MqAtWnoGPWrx6humgzMusgVqj6jjhahLmQ5xFf.d7To0S5M2CaMXNec9n6m1LfHo0QJhToJomAmLw0uXiVWvHBvbXiiCAB42u117oVG8PCTMcSSgK6yAz_MPZgNhFggyIfnZfyBH8G87ak34FUKRjFmtN41IauF2wkc; NTES_PASSPORT=Od5Kb36bac.G_Ttl4LRnxIx3INeOLvOz2rdPrFD_Y4SeyYwuJyZwtT6B66XSXxYMrog1EnWmvhgeQoBrwqMsDg7RPANP8ND_uqpdYjXIyOoXLO9FYNH.8liOeZKdMf6cYJsxz5EGPmhC2C5J9jCBk5Yfm8P5unVAgxGWRuIunquIRx7AeIC4Untsn; S_INFO=1597200489|0|2&10##|ad_jztest501; P_INFO=ad_jztest501@163.com|1597200489|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest501@163.com"
}

headerscookies9 = {
    "Cookie": "language=cn; NTES_SESS=M4EHkxe5bNl0hkuni82cBBKjgoVWvHr5r5RbQ.8RYX_cLoieELdifjI_IIcuchoDmNRUoS.Vm2htE40uE7AnSHb_oMhk3QBDOc6QOQopoh9BL7KfRw3Gwa7KK0pGs4LMMWQf.q806ESyyiZ_xpeFE8lZr.qdSezfRVs.mjxdmIvuxoruFKOvc8rd1P4upK0rN; NTES_PASSPORT=ivMquUpUS64chMbEYIiiyKS6Y4_7cA._S3Qh3eHzNm_8FNEUgF1EKWRaRR0_0CNp3So8Hpwl3an.9wa3ESpoHDB.hOJhcJHzUStQNy0xFiw0liVeNJfLc7Q4_ykzKwgDosxe93iTwCvTgtWTKTekm.gU1x8lqZJ3p8k1fZOBKoFEnptOeWBUPc9oq; S_INFO=1597200577|0|2&10##|ad_jztest500; P_INFO=ad_jztest500@163.com|1597200577|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest500@163.com"
}
headerscookies10 = {
    "Cookie": "language=cn; NTES_SESS=W5V38uvKtCRq6dFPWaWX2QH4EWns8utH_6e8Go8VimmZvcIdRvqIerXQnqMQxNxH_.9l9r_zsmBceFSTEIaaUhGmFPlnpm1sMkG4_3Ta4yooAtQ0wK7KcCgsBU5mqxo_mVWhlCCRQYABOosshe70iH4iUCQkxhlXOX.9BVshHkLiq23NLCBwUnYKAnlYkGh5V; NTES_PASSPORT=tWcykOjoRYh3hjWoythOTTq0XWIbhKSgLfUHMaq4uYfncDZbfciZJUMjOi6j171x3Fqdh9vHu0BOM2tyTgZxOvdaBRNvj6QGuP_YxAaBMn5do.onmHJWjAIB3zEjckHtcvMKZD.OA5vT2LQgOmd0Lf8owUEhvxkBfay76poq0qN0b; S_INFO=1597200692|0|2&10##|montest13; P_INFO=montest13@163.com|1597200692|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||montest13@163.com"
}
headerscookies11 = {
    "Cookie": "language=cn; NTES_SESS=J.f8uWwLc.eKclWE_FtLm56AeK0X3LNzbracMIlafeG7x19LOxv956_G__7y7X1EYBgaA7P7GnBFlG5xotA0MSaG1JXm4MqEQ7BMQM1g1XpqxnH5aA4jASnHH8gjZKxJJbM5ITl8BOWRR93GzgL.Ol_FZKUKYWgpaJmcDb8LkR2j6rTnSk_W4_8RShyv1dUXn; NTES_PASSPORT=VuF79OvqEaWkOc4c2RYpFiHI2sVqn1x_Cmp0ml5UoNu7LoieELdifjI_IIcuchoDmVpAW4VJJWcf9elw9s4s7fux09w0Bw5UeGHpo.cPLVOcnVKlowZCBqOreO8NVq8mkVsIN4ttFDw1Jc9DsoRfeswYK.hdiW2BIj.72MMlOLo2hC_nVSRXcDtAW; S_INFO=1597200780|0|2&10##|ad_jztest400; P_INFO=ad_jztest400@163.com|1597200780|1|hongcai|00&99|bej&1594640931&hongcai#bej&null#10#0#0|&0||ad_jztest400@163.com"
}
headerscookies12 = {
    "Cookie": "language=cn; NTES_SESS=r62uSD4hzv9aUcFtlbaXADoauK3ZNfu..KMp3BpUz00nbtsWYb2sMPoHaB26VXGA5doozeVuqMpLPIm5b5y32GBxI38soP3EU.h4eReuzjpceVDjHSMMitQPHdrS3U0TjJ.r4is5guK.LjRVkjdiUEbzmnO8E1RD6_LPrV2kioICmeAAFlJkpmt39PzteUt9H; NTES_PASSPORT=.y2MKf9kdDJwcnFel3pXmJ1wJsQiiV2BuGHWCQvaD_Gm1TyoG1cyPHFbMvcdq5wL6aZu79RN3XcfCVgSnwkWfaXZzLX8OZNmAEfQZV3FJBl3COtt0XUwkJPsjQ7cOD131ySgZM8WK4a2ERocLZg4l04NN9XuFA9wOSm4BmeR9_qJwYlV6OvGlNIbt; S_INFO=1597203285|0|2&10##|montest299; P_INFO=montest299@163.com|1597203285|1|hongcai|00&99|bej&1597203210&hongcai#bej&null#10#0#0|&0|hongcai|montest299@163.com"
}



list = [headerscookies0, headerscookies1, headerscookies2, headerscookies3, headerscookies4, headerscookies5,
        headerscookies6, headerscookies7, headerscookies8, headerscookies9, headerscookies10]


# post_publicThread = "https://hc-expert-test.ws.netease.com/api/proficient/thread/addThread"

def post_pathSpecial():
    params_publicThread = {
        "categoryId": "1",
        "title": "专家方案分布9.2.0——水晶宫 VS 南安普敦",
        "price": "28",
        # "matches":'[{"matchInfoId":1000000000632860,"recommendPlayList":[{"playId": 1000000000601025,"predictItemIds":[1000000001200909],"playMetaId":1}]}
        "content": '新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新新马格拉色球双色球双色球双色双色球双色球双色双色球双色球双色球色球双色球双色球双色球双色球双色球双色双色双色球双色球双色球双色球双色球双色球双色双色球双色球双色双色球双色球双色球色球双色球双色球双色球双色球双色球双色双色双色球双色球双色球双色球双色球双色球双色双色球双色球双色双色球双色球双色球色球双色球双色球双色球双色球双色球双色双色双色球双色球双色球双色球双色球双色球双色双色球双色球双色双色球双色球双色球色球双色球双色球双色球双色球双色球双色双色双色球双色球双色球双色球双色球双色球双色双色球双色球双色双色球双色球双色球色球双色球双色球双色球双色球双色球双色双色双色球双色球双色球双色球双色球双色球双色双色球双色球双色双色球双色球双色球色球双色球双色球双色球',
        # "buyReason": "自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发自动化测试发文自动化测试发文自动化测试发自动化测试发文自动化测试发文自动化测试发自动化测试发文自动化测试发文自动化测试发自动化测试发文自动化测试发文自动化测试发自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文",
        "isTempSave": "0",
        "businessTypeId": "0"
    }
    params = params_publicThread
    path_name = "https://hc-expert-test.ws.netease.com/api/proficient/thread/addThread"
    for i in list[:9]:
        headers = i
        print(i)
        res = requests.post(path_name, params=params, headers=headers, verify=False)
        print(res.text)
    return


post_pathSpecial()
