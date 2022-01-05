# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class BindOrganizationMemberAuthAccountRequest(AbstractModel):
    """BindOrganizationMemberAuthAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param MemberUin: 成员Uin。
        :type MemberUin: int
        :param PolicyId: 策略ID。
        :type PolicyId: int
        :param OrgSubAccountUins: 组织子账号Uin。
        :type OrgSubAccountUins: list of int
        """
        self.MemberUin = None
        self.PolicyId = None
        self.OrgSubAccountUins = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.PolicyId = params.get("PolicyId")
        self.OrgSubAccountUins = params.get("OrgSubAccountUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOrganizationMemberAuthAccountResponse(AbstractModel):
    """BindOrganizationMemberAuthAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateOrganizationMemberRequest(AbstractModel):
    """CreateOrganizationMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param PolicyType: 关系策略
        :type PolicyType: str
        :param PermissionIds: 关系权限
        :type PermissionIds: list of int non-negative
        :param NodeId: 需要调节的节点
        :type NodeId: int
        :param AccountName: 账号名
        :type AccountName: str
        :param Remark: 备注
        :type Remark: str
        :param RecordId: 重试创建传记录ID
        :type RecordId: int
        """
        self.Name = None
        self.PolicyType = None
        self.PermissionIds = None
        self.NodeId = None
        self.AccountName = None
        self.Remark = None
        self.RecordId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.PolicyType = params.get("PolicyType")
        self.PermissionIds = params.get("PermissionIds")
        self.NodeId = params.get("NodeId")
        self.AccountName = params.get("AccountName")
        self.Remark = params.get("Remark")
        self.RecordId = params.get("RecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberResponse(AbstractModel):
    """CreateOrganizationMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")