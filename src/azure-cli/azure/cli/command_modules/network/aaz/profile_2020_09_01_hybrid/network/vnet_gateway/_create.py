# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network vnet-gateway create",
)
class Create(AAZCommand):
    """Create a virtual network gateway.

    :example: Create a basic virtual network gateway for site-to-site connectivity.
        az network vnet-gateway create -g MyResourceGroup -n MyVnetGateway --public-ip-address MyGatewayIp --vnet MyVnet --gateway-type Vpn --sku VpnGw1 --vpn-type RouteBased --no-wait

    :example: Create a basic virtual network gateway that provides point-to-site connectivity with a RADIUS secret that matches what is configured on a RADIUS server.
        az network vnet-gateway create -g MyResourceGroup -n MyVnetGateway --public-ip-address MyGatewayIp --vnet MyVnet --gateway-type Vpn --sku VpnGw1 --vpn-type RouteBased --address-prefixes 40.1.0.0/24 --client-protocol IkeV2 SSTP --radius-secret 111_aaa --radius-server 30.1.1.15 --vpn-gateway-generation Generation1

    :example: Create a basic virtual network gateway with multi authentication
        az network vnet-gateway create -g MyResourceGroup -n MyVnetGateway --public-ip-address MyGatewayIp --vnet MyVnet --gateway-type Vpn --sku VpnGw1 --vpn-type RouteBased --address-prefixes 40.1.0.0/24 --client-protocol OpenVPN --radius-secret 111_aaa --radius-server 30.1.1.15 --aad-issuer https://sts.windows.net/00000-000000-00000-0000-000/ --aad-tenant https://login.microsoftonline.com/000 --aad-audience 0000-000 --root-cert-name root-cert --root-cert-data "root-cert.cer" --vpn-auth-type AAD Certificate Radius

    :example: Create a virtual network gateway.
        az network vnet-gateway create --gateway-type Vpn --location westus2 --name MyVnetGateway --no-wait --public-ip-addresses myVGPublicIPAddress --resource-group MyResourceGroup --sku Basic --vnet MyVnet --vpn-type PolicyBased
    """

    _aaz_info = {
        "version": "2018-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualnetworkgateways/{}", "2018-11-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the VNet gateway.",
            required=True,
        )
        _args_schema.location = AAZResourceLocationArg(
            help="Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.gateway_default_site = AAZStrArg(
            options=["--gateway-default-site"],
            help="Name or ID of a local network gateway representing a local network site with default routes.",
        )
        _args_schema.gateway_type = AAZStrArg(
            options=["--gateway-type"],
            help="The gateway type.",
            default="Vpn",
            enum={"ExpressRoute": "ExpressRoute", "Vpn": "Vpn"},
        )
        _args_schema.ip_configurations = AAZListArg(
            options=["--ip-configurations"],
            help="IP configurations for virtual network gateway.",
        )
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            help="VNet gateway SKU.",
            default="Basic",
            enum={"Basic": "Basic", "ErGw1AZ": "ErGw1AZ", "ErGw2AZ": "ErGw2AZ", "ErGw3AZ": "ErGw3AZ", "HighPerformance": "HighPerformance", "Standard": "Standard", "UltraPerformance": "UltraPerformance", "VpnGw1": "VpnGw1", "VpnGw1AZ": "VpnGw1AZ", "VpnGw2": "VpnGw2", "VpnGw2AZ": "VpnGw2AZ", "VpnGw3": "VpnGw3", "VpnGw3AZ": "VpnGw3AZ"},
        )
        _args_schema.vpn_type = AAZStrArg(
            options=["--vpn-type"],
            help="VPN routing type.",
            default="RouteBased",
            enum={"PolicyBased": "PolicyBased", "RouteBased": "RouteBased"},
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
        )

        ip_configurations = cls._args_schema.ip_configurations
        ip_configurations.Element = AAZObjectArg()

        _element = cls._args_schema.ip_configurations.Element
        _element.etag = AAZStrArg(
            options=["etag"],
            help="A unique read-only string that changes whenever the resource is updated.",
        )
        _element.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the resource that is unique within a resource group. This name can be used to access the resource.",
        )
        _element.private_ip_allocation_method = AAZStrArg(
            options=["private-ip-allocation-method"],
            help="The private IP address allocation method.",
            enum={"Dynamic": "Dynamic", "Static": "Static"},
        )
        _element.public_ip_address = AAZStrArg(
            options=["public-ip-address"],
            help="The reference to the public IP resource.",
        )
        _element.subnet = AAZStrArg(
            options=["subnet"],
            help="test",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "BGP Peering"

        _args_schema = cls._args_schema
        _args_schema.asn = AAZIntArg(
            options=["--asn"],
            arg_group="BGP Peering",
            help="Autonomous System Number to use for the BGP settings.",
        )
        _args_schema.bgp_peering_address = AAZStrArg(
            options=["--bgp-peering-address"],
            arg_group="BGP Peering",
            help="IP address to use for BGP peering.",
        )
        _args_schema.peer_weight = AAZIntArg(
            options=["--peer-weight"],
            arg_group="BGP Peering",
            help="Weight (0-100) added to routes learned through BGP peering.",
        )
        _args_schema.enable_bgp = AAZBoolArg(
            options=["--enable-bgp"],
            arg_group="BGP Peering",
            help="Enable BGP (Border Gateway Protocol).",
        )

        # define Arg Group "Parameters"

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.active = AAZBoolArg(
            options=["--active"],
            arg_group="Properties",
            help="ActiveActive flag.",
        )
        _args_schema.sku_tier = AAZStrArg(
            options=["--sku-tier"],
            arg_group="Properties",
            help="Gateway SKU tier.",
            enum={"Basic": "Basic", "ErGw1AZ": "ErGw1AZ", "ErGw2AZ": "ErGw2AZ", "ErGw3AZ": "ErGw3AZ", "HighPerformance": "HighPerformance", "Standard": "Standard", "UltraPerformance": "UltraPerformance", "VpnGw1": "VpnGw1", "VpnGw1AZ": "VpnGw1AZ", "VpnGw2": "VpnGw2", "VpnGw2AZ": "VpnGw2AZ", "VpnGw3": "VpnGw3", "VpnGw3AZ": "VpnGw3AZ"},
        )

        # define Arg Group "Root Cert Authentication"

        _args_schema = cls._args_schema
        _args_schema.vpn_client_root_certificates = AAZListArg(
            options=["--vpn-client-root-certificates"],
            arg_group="Root Cert Authentication",
            help="VpnClientRootCertificate for virtual network gateway.",
        )

        vpn_client_root_certificates = cls._args_schema.vpn_client_root_certificates
        vpn_client_root_certificates.Element = AAZObjectArg()

        _element = cls._args_schema.vpn_client_root_certificates.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the resource that is unique within a resource group. This name can be used to access the resource.",
        )
        _element.public_cert_data = AAZStrArg(
            options=["public-cert-data"],
            help="The certificate public data.",
            required=True,
        )

        # define Arg Group "Sku"

        # define Arg Group "VPN Client"

        _args_schema = cls._args_schema
        _args_schema.radius_server = AAZStrArg(
            options=["--radius-server"],
            arg_group="VPN Client",
            help="Radius server address to connect to.",
        )
        _args_schema.radius_secret = AAZStrArg(
            options=["--radius-secret"],
            arg_group="VPN Client",
            help="Radius secret to use for authentication.",
        )
        _args_schema.address_prefixes = AAZListArg(
            options=["--address-prefixes"],
            singular_options=["--address-prefix"],
            arg_group="VPN Client",
            help="Space-separated list of CIDR prefixes representing the address space for the P2S Vpnclient.",
        )
        _args_schema.client_protocol = AAZListArg(
            options=["--client-protocol"],
            arg_group="VPN Client",
            help="Protocols to use for connecting.  Allowed values: IkeV2, OpenVPN, SSTP.",
        )

        address_prefixes = cls._args_schema.address_prefixes
        address_prefixes.Element = AAZStrArg()

        client_protocol = cls._args_schema.client_protocol
        client_protocol.Element = AAZStrArg(
            enum={"IkeV2": "IkeV2", "OpenVPN": "OpenVPN", "SSTP": "SSTP"},
        )

        # define Arg Group "VpnClientConfiguration"
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.VirtualNetworkGatewaysCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class VirtualNetworkGatewaysCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualNetworkGatewayName", self.ctx.args.name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("activeActive", AAZBoolType, ".active")
                properties.set_prop("bgpSettings", AAZObjectType)
                properties.set_prop("enableBgp", AAZBoolType, ".enable_bgp")
                properties.set_prop("gatewayDefaultSite", AAZObjectType)
                properties.set_prop("gatewayType", AAZStrType, ".gateway_type")
                properties.set_prop("ipConfigurations", AAZListType, ".ip_configurations")
                properties.set_prop("sku", AAZObjectType)
                properties.set_prop("vpnClientConfiguration", AAZObjectType)
                properties.set_prop("vpnType", AAZStrType, ".vpn_type")

            bgp_settings = _builder.get(".properties.bgpSettings")
            if bgp_settings is not None:
                bgp_settings.set_prop("asn", AAZIntType, ".asn")
                bgp_settings.set_prop("bgpPeeringAddress", AAZStrType, ".bgp_peering_address")
                bgp_settings.set_prop("peerWeight", AAZIntType, ".peer_weight")

            gateway_default_site = _builder.get(".properties.gatewayDefaultSite")
            if gateway_default_site is not None:
                gateway_default_site.set_prop("id", AAZStrType, ".gateway_default_site")

            ip_configurations = _builder.get(".properties.ipConfigurations")
            if ip_configurations is not None:
                ip_configurations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.ipConfigurations[]")
            if _elements is not None:
                _elements.set_prop("etag", AAZStrType, ".etag")
                _elements.set_prop("id", AAZStrType, ".id")
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties.ipConfigurations[].properties")
            if properties is not None:
                properties.set_prop("privateIPAllocationMethod", AAZStrType, ".private_ip_allocation_method")
                properties.set_prop("publicIPAddress", AAZObjectType)
                properties.set_prop("subnet", AAZObjectType)

            public_ip_address = _builder.get(".properties.ipConfigurations[].properties.publicIPAddress")
            if public_ip_address is not None:
                public_ip_address.set_prop("id", AAZStrType, ".public_ip_address")

            subnet = _builder.get(".properties.ipConfigurations[].properties.subnet")
            if subnet is not None:
                subnet.set_prop("id", AAZStrType, ".subnet")

            sku = _builder.get(".properties.sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".sku")
                sku.set_prop("tier", AAZStrType, ".sku_tier")

            vpn_client_configuration = _builder.get(".properties.vpnClientConfiguration")
            if vpn_client_configuration is not None:
                vpn_client_configuration.set_prop("radiusServerAddress", AAZStrType, ".radius_server")
                vpn_client_configuration.set_prop("radiusServerSecret", AAZStrType, ".radius_secret")
                vpn_client_configuration.set_prop("vpnClientAddressPool", AAZObjectType)
                vpn_client_configuration.set_prop("vpnClientProtocols", AAZListType, ".client_protocol")
                vpn_client_configuration.set_prop("vpnClientRootCertificates", AAZListType, ".vpn_client_root_certificates")

            vpn_client_address_pool = _builder.get(".properties.vpnClientConfiguration.vpnClientAddressPool")
            if vpn_client_address_pool is not None:
                vpn_client_address_pool.set_prop("addressPrefixes", AAZListType, ".address_prefixes")

            address_prefixes = _builder.get(".properties.vpnClientConfiguration.vpnClientAddressPool.addressPrefixes")
            if address_prefixes is not None:
                address_prefixes.set_elements(AAZStrType, ".")

            vpn_client_protocols = _builder.get(".properties.vpnClientConfiguration.vpnClientProtocols")
            if vpn_client_protocols is not None:
                vpn_client_protocols.set_elements(AAZStrType, ".")

            vpn_client_root_certificates = _builder.get(".properties.vpnClientConfiguration.vpnClientRootCertificates")
            if vpn_client_root_certificates is not None:
                vpn_client_root_certificates.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.vpnClientConfiguration.vpnClientRootCertificates[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties.vpnClientConfiguration.vpnClientRootCertificates[].properties")
            if properties is not None:
                properties.set_prop("publicCertData", AAZStrType, ".public_cert_data", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType()
            _schema_on_200_201.id = AAZStrType()
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.active_active = AAZBoolType(
                serialized_name="activeActive",
            )
            properties.bgp_settings = AAZObjectType(
                serialized_name="bgpSettings",
            )
            properties.enable_bgp = AAZBoolType(
                serialized_name="enableBgp",
            )
            properties.gateway_default_site = AAZObjectType(
                serialized_name="gatewayDefaultSite",
            )
            _CreateHelper._build_schema_sub_resource_read(properties.gateway_default_site)
            properties.gateway_type = AAZStrType(
                serialized_name="gatewayType",
            )
            properties.ip_configurations = AAZListType(
                serialized_name="ipConfigurations",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
            )
            properties.sku = AAZObjectType()
            properties.vpn_client_configuration = AAZObjectType(
                serialized_name="vpnClientConfiguration",
            )
            properties.vpn_type = AAZStrType(
                serialized_name="vpnType",
            )

            bgp_settings = cls._schema_on_200_201.properties.bgp_settings
            bgp_settings.asn = AAZIntType()
            bgp_settings.bgp_peering_address = AAZStrType(
                serialized_name="bgpPeeringAddress",
            )
            bgp_settings.peer_weight = AAZIntType(
                serialized_name="peerWeight",
            )

            ip_configurations = cls._schema_on_200_201.properties.ip_configurations
            ip_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.ip_configurations.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200_201.properties.ip_configurations.Element.properties
            properties.private_ip_allocation_method = AAZStrType(
                serialized_name="privateIPAllocationMethod",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_address = AAZObjectType(
                serialized_name="publicIPAddress",
            )
            _CreateHelper._build_schema_sub_resource_read(properties.public_ip_address)
            properties.subnet = AAZObjectType()
            _CreateHelper._build_schema_sub_resource_read(properties.subnet)

            sku = cls._schema_on_200_201.properties.sku
            sku.capacity = AAZIntType()
            sku.name = AAZStrType()
            sku.tier = AAZStrType()

            vpn_client_configuration = cls._schema_on_200_201.properties.vpn_client_configuration
            vpn_client_configuration.radius_server_address = AAZStrType(
                serialized_name="radiusServerAddress",
            )
            vpn_client_configuration.radius_server_secret = AAZStrType(
                serialized_name="radiusServerSecret",
            )
            vpn_client_configuration.vpn_client_address_pool = AAZObjectType(
                serialized_name="vpnClientAddressPool",
            )
            vpn_client_configuration.vpn_client_ipsec_policies = AAZListType(
                serialized_name="vpnClientIpsecPolicies",
            )
            vpn_client_configuration.vpn_client_protocols = AAZListType(
                serialized_name="vpnClientProtocols",
            )
            vpn_client_configuration.vpn_client_revoked_certificates = AAZListType(
                serialized_name="vpnClientRevokedCertificates",
            )
            vpn_client_configuration.vpn_client_root_certificates = AAZListType(
                serialized_name="vpnClientRootCertificates",
            )

            vpn_client_address_pool = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_address_pool
            vpn_client_address_pool.address_prefixes = AAZListType(
                serialized_name="addressPrefixes",
            )

            address_prefixes = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_address_pool.address_prefixes
            address_prefixes.Element = AAZStrType()

            vpn_client_ipsec_policies = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_ipsec_policies
            vpn_client_ipsec_policies.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_ipsec_policies.Element
            _element.dh_group = AAZStrType(
                serialized_name="dhGroup",
                flags={"required": True},
            )
            _element.ike_encryption = AAZStrType(
                serialized_name="ikeEncryption",
                flags={"required": True},
            )
            _element.ike_integrity = AAZStrType(
                serialized_name="ikeIntegrity",
                flags={"required": True},
            )
            _element.ipsec_encryption = AAZStrType(
                serialized_name="ipsecEncryption",
                flags={"required": True},
            )
            _element.ipsec_integrity = AAZStrType(
                serialized_name="ipsecIntegrity",
                flags={"required": True},
            )
            _element.pfs_group = AAZStrType(
                serialized_name="pfsGroup",
                flags={"required": True},
            )
            _element.sa_data_size_kilobytes = AAZIntType(
                serialized_name="saDataSizeKilobytes",
                flags={"required": True},
            )
            _element.sa_life_time_seconds = AAZIntType(
                serialized_name="saLifeTimeSeconds",
                flags={"required": True},
            )

            vpn_client_protocols = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_protocols
            vpn_client_protocols.Element = AAZStrType()

            vpn_client_revoked_certificates = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_revoked_certificates
            vpn_client_revoked_certificates.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.thumbprint = AAZStrType()

            vpn_client_root_certificates = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_root_certificates
            vpn_client_root_certificates.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_root_certificates.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )

            properties = cls._schema_on_200_201.properties.vpn_client_configuration.vpn_client_root_certificates.Element.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_cert_data = AAZStrType(
                serialized_name="publicCertData",
                flags={"required": True},
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Create"]