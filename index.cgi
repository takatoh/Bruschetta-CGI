#!/usr/bin/env ruby
# encoding: utf-8

require 'cgi'
require 'erb'
require 'httpclient'
require 'json'


@cgi = CGI.new
@client = HTTPClient.new
config = JSON.parse(File.read("./config.json"))
@title = config["siteTitle"]
@server = config["server"]


def main
  if !@cgi["id"].empty?
    book_detail(@cgi["id"].to_i)
  elsif !@cgi["search"].empty?
    search(@cgi["search"])
  else
    page = @cgi["page"].empty? ? 1 : @cgi["page"].to_i
    index(page)
  end
end


def index(page)
  offset = 25 * (page - 1)
  json = @client.get("http://#{@server}/api/books/?limit=25&offset=#{offset.to_s}").body
  @books = JSON.parse(json)["books"]

  render("index")
end


def search(title_or_author)
  query = "both=" + CGI.escape(title_or_author)
  json = @client.get("http://#{@server}/api/search/?#{query}").body
  @books = JSON.parse(json)["books"]

  render("index")
end


def book_detail(id)
  json = @client.get("http://#{@server}/api/book/#{id.to_s}/").body
  @book = JSON.parse(json)["books"][0]

  render("detail")
end


def render(template_name)
  template = File.read("./views/#{template_name}.erb")
  erb = ERB.new(template)
  print_header
  print erb.result
end


def print_header
  print "content-type: text/html\n\n"
end


def title_with_vol(book)
  unless book["volume"].empty?
    "#{book["title"]} [#{book["volume"]}]"
  else
    book["title"]
  end
end



main
